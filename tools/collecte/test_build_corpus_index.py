"""Controles de l'index canonique du corpus. Aucune requete reseau,
aucune ecriture hors du fichier d'index lui-meme.

Lancer : python test_build_corpus_index.py
"""
import json
import unittest
from collections import Counter
from pathlib import Path

import build_corpus_index as bci


class TestGenerationAndValidation(unittest.TestCase):
    def test_generation_is_valid(self):
        corpora = bci.build_index()
        bci.validate(corpora)  # ne doit lever aucune ValidationError

    def test_generation_is_stable(self):
        first = bci.build_index()
        second = bci.build_index()
        ids1 = sorted(c.corpus_id for c in first)
        ids2 = sorted(c.corpus_id for c in second)
        self.assertEqual(ids1, ids2)
        counts1 = {c.corpus_id: c.file_count for c in first}
        counts2 = {c.corpus_id: c.file_count for c in second}
        self.assertEqual(counts1, counts2)

    def test_no_duplicate_corpus_id(self):
        corpora = bci.build_index()
        ids = [c.corpus_id for c in corpora]
        dupes = [cid for cid, n in Counter(ids).items() if n > 1]
        self.assertEqual(dupes, [], f"corpus_id dupliques: {dupes}")

    def test_totals_match_recount(self):
        corpora = bci.build_index()
        for c in corpora:
            if not c.root_path:
                continue
            root = bci.REPO_ROOT / c.root_path
            if c.collection_method == "historique" and root == bci.SOURCES_DIR / c.concurrent:
                files = bci.scan_files(root, exclude_top=bci.RESERVED_SUBDIRS)
                files = [p for p in files if not (p.parent == root and p.name in bci.META_FILES_AT_ROOT)]
            else:
                files = bci.scan_files(root)
            self.assertEqual(len(files), c.file_count, f"{c.corpus_id}: total incoherent avec le disque")


class TestOpenfireDistinct(unittest.TestCase):
    def test_three_distinct_corpora(self):
        corpora = bci.build_index()
        of = [c for c in corpora if c.concurrent == "openfire"]
        ids = {c.corpus_id for c in of}
        self.assertEqual(ids, {"openfire_zendesk", "openfire_odoo", "openfire_marketing"})
        roots = [c.root_path for c in of]
        self.assertEqual(len(roots), len(set(roots)), "les corpus openfire partagent un root_path")

    def test_no_implicit_ranking_fields(self):
        corpora = bci.build_index()
        of = [c for c in corpora if c.concurrent == "openfire"]
        forbidden = {"ancien", "nouveau", "principal", "secondaire", "obsolete", "obsolète",
                     "plus complet", "plus fiable", "meilleur"}
        for c in of:
            blob = " ".join(c.notes).lower()
            for word in forbidden:
                self.assertNotIn(word, blob, f"{c.corpus_id}: vocabulaire interpretatif trouve ({word})")


class TestCoverageHoles(unittest.TestCase):
    def test_tolteck_help_documented_not_collected(self):
        corpora = bci.build_index()
        c = next(x for x in corpora if x.corpus_id == "tolteck_help")
        self.assertEqual(c.coverage_status, "not_collected_documented")
        self.assertEqual(c.file_count, 0)
        self.assertTrue(any("TLS" in n for n in c.notes))

    def test_leobati_help_documented_not_collected(self):
        corpora = bci.build_index()
        c = next(x for x in corpora if x.corpus_id == "leobati_help")
        self.assertEqual(c.coverage_status, "not_collected_documented")
        self.assertEqual(c.file_count, 0)
        self.assertTrue(any("onglets" in n or "SPA" in n for n in c.notes))

    def test_tolteck_marketing_was_collected(self):
        corpora = bci.build_index()
        c = next(x for x in corpora if x.corpus_id == "tolteck_marketing")
        self.assertEqual(c.coverage_status, "collected")
        self.assertGreater(c.file_count, 0)


class TestLegalExclusions(unittest.TestCase):
    def test_16_certain_1_ambiguous(self):
        certain = [e for e in bci.LEGAL_EXCLUSIONS if e[2] == "certain"]
        ambiguous = [e for e in bci.LEGAL_EXCLUSIONS if e[2] == "ambiguous"]
        self.assertEqual(len(certain), 16)
        self.assertEqual(len(ambiguous), 1)

    def test_all_exclusions_reference_existing_files(self):
        for relpath, _motif, _status in bci.LEGAL_EXCLUSIONS:
            p = bci.SOURCES_DIR / relpath
            self.assertTrue(p.exists(), f"exclusion introuvable sur disque: {relpath}")

    def test_exclusions_attached_to_correct_corpus_only(self):
        corpora = bci.build_index()
        for c in corpora:
            for exc in c.analysis_exclusions:
                self.assertTrue(
                    exc["path"].startswith(f"01-discovery/concurrents/sources/{c.concurrent}/"),
                    f"{c.corpus_id} porte une exclusion d'un autre concurrent: {exc['path']}",
                )

    def test_sellsy_ambiguous_case_not_certain(self):
        corpora = bci.build_index()
        c = next(x for x in corpora if x.corpus_id == "sellsy_marketing")
        bareme = [e for e in c.analysis_exclusions if "bareme" in e["path"]]
        self.assertEqual(len(bareme), 1)
        self.assertEqual(bareme[0]["status"], "ambiguous")


class TestSixReferenceCases(unittest.TestCase):
    """Verifie que les 6 cas cites dans la mission sont representables
    sans branche codee en dur par concurrent."""

    def test_sellsy_help_plus_marketing(self):
        corpora = {c.corpus_id: c for c in bci.build_index()}
        self.assertIn("sellsy_help", corpora)
        self.assertIn("sellsy_marketing", corpora)
        self.assertTrue(corpora["sellsy_help"].editorial_taxonomy)

    def test_progbat_flat_help_plus_marketing(self):
        corpora = {c.corpus_id: c for c in bci.build_index()}
        self.assertEqual(corpora["progbat_help"].collection_method, "automatique")
        self.assertGreater(corpora["progbat_marketing"].file_count, 0)

    def test_openfire_three_corpora(self):
        corpora = {c.corpus_id: c for c in bci.build_index()}
        for cid in ("openfire_zendesk", "openfire_odoo", "openfire_marketing"):
            self.assertIn(cid, corpora)

    def test_vertuoza_multi_locale_marketing(self):
        corpora = {c.corpus_id: c for c in bci.build_index()}
        self.assertGreaterEqual(len(corpora["vertuoza_marketing"].locales_observed), 3)

    def test_tolteck_marketing_collected_help_not(self):
        corpora = {c.corpus_id: c for c in bci.build_index()}
        self.assertEqual(corpora["tolteck_help"].coverage_status, "not_collected_documented")
        self.assertEqual(corpora["tolteck_marketing"].coverage_status, "collected")

    def test_leobati_marketing_collected_help_not(self):
        corpora = {c.corpus_id: c for c in bci.build_index()}
        self.assertEqual(corpora["leobati_help"].coverage_status, "not_collected_documented")
        self.assertEqual(corpora["leobati_marketing"].coverage_status, "collected")


if __name__ == "__main__":
    unittest.main()
