---
source: https://help.sellsy.com/fr/articles/10308956-les-differents-types-d-id-sur-l-api-v1
categorie: Intégrations et API
titre: Les différents types d’ID sur l’API V1
date_recuperation: 2026-09-05
---

# Les différents types d’ID sur l’API V1

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159291251/761aaef37f7fc38521bbac64c780/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=f06cad0faa13aed0a890abe36c079c83d3aa1c134ea05d161c01d26929925de9&req=diEiH8t3nINaWPMW1HO4zZIj%2BLTby6pK1YDVYJQvSNoWra2GnPoFd62r40WH%0AwgBLPE376xmq3QA%2FSK4%3D%0A)

### 


___________________________________________________________

### People ID

C’est l’ID du contact, vous pouvez le retrouver directement dans l’URL d'une fiche contact. 

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1306072701/e8750187d3f259edac801d2aec5c/contact.png?expires=1788635700&signature=bd4018bb0880a308ff3cd432b7614d6b773dba0f3f81e05519375a6fc2921b72&req=dSMnEMl5n4ZfWPMW1HO4zbVUSdxKVrKz4uIDTZYVUJY8qasl7ZZLZBcoTerO%0AIGdO%2FyRv7bQJjQSNYp8%3D%0A)

___________________________________________________________

### Third ID

C’est l’ID de la société (client, prospect ou fournisseur), vous pouvez le retrouver directement dans l’URL d'une fiche société. 

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1306073167/eede59f577d722934ed1a5941a52/third.png?expires=1788635700&signature=2fbd328e54ae6dd9c7b18022aab6cba722ba8db90467bb8668d4ae83dce56456&req=dSMnEMl5noBZXvMW1HO4zZ5pS2yuOaMg%2BgjTvU0xP50U%2FLhxB50h0BXO4dPt%0AFDMw%2F%2Fs1VldjWo6Dmlk%3D%0A)

___________________________________________________________

### Thirdcontact ID

C’est un ID de liaison entre la société et le contact, vous pouvez l’obtenir en faisant un GET sur le contact ciblé. 

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1306089072/eccb7243b044af578b404e32e2bc/Thirdcontact_1.png?expires=1788635700&signature=6fd18d6bfbf1b847556bb50c7e8edf80dc7b756116b3de31cc5c892bce64553f&req=dSMnEMl2lIFYW%2FMW1HO4zd8APVX0Zh2jIQSpBGrH5dXJcFlx2WOZ%2Bf%2BBAuxE%0A7jhr0FjccVxJ94oR7FA%3D%0A)

Sur un GET contact en API V1, vous pouvez récupérer les informations du contact en renseignant l'ID du client (thirdid) et l'ID de liaison (thirdcontactid).

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1306091139/f717fec5bc98c69e983dd04feadd/Thirdcontact_2.png?expires=1788635700&signature=9a128029efc48374bb349604c05dd700c301c5fdd47c5f11bac9d07571096643&req=dSMnEMl3nIBcUPMW1HO4zWY5O6TwT3BZQCKv2X%2Bws1ZopRdAYeWSYzQOCFin%0ArtQvCCZhcHWnqn%2BtZZI%3D%0A)

Mis a jour le : 13/03/2026
