# Blocklists / Listes de blocage

[![Build](https://img.shields.io/github/actions/workflow/status/GloomyD/blocklists/build.yml?branch=main)](https://github.com/GloomyD/blocklists/actions)
[![License](https://img.shields.io/github/license/GloomyD/blocklists)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/GloomyD/blocklists)](https://github.com/GloomyD/blocklists/commits/main)
[![Made in France](https://img.shields.io/badge/Made%20in-France-blue)]()
[![EU Context](https://img.shields.io/badge/Scope-Europe-informational)]()

Curated filter lists for **uBlacklist** and **NextDNS**.

---
**Curated filter lists for uBlacklist and NextDNS / Listes de filtres pour uBlacklist et NextDNS**

---

## 🌍 English

### What is this?
Some websites distribute misleading content, large-scale low-quality AI-generated content (“AI slop”), SEO spam, or politically motivated disinformation.

This repository provides curated domain blocklists compatible with:

- **uBlacklist** (browser search filtering)
- **NextDNS** (DNS-level filtering)

The project is maintained from **France** and includes sources related to **European digital interference monitoring**.


### Supported Tools
- **uBlacklist**
Browser extension (Chrome, Firefox, Safari) that hides unwanted domains from search results.
  [Official website](https://ublacklist.github.io/)
- **NextDNS**
DNS resolver that blocks trackers, ads, and unwanted content at the network level.
  [Official website](https://nextdns.io/?from=zjmur6v8)

### How to Use
You can:
- Manually add sites to block
- Subscribe to public filter lists (see above)
- Copy-paste lists from this repository

## 🔐 Using with NextDNS

The domain lists for NextDNS are available in the `dist/` directory of this repository.

Files:
- `dist/complotistes.nextdns.txt`
- `dist/ia-seo.nextdns.txt`
- `dist/ingerences.nextdns.txt`

Each file contains one domain per line and is intended to be used as a denylist.

To use them in NextDNS:

1. Go to your NextDNS configuration.
2. Open the **Denylist** section.
3. Copy and paste domains from the corresponding `.nextdns.txt` file.

### 🔐 Using with uBlacklist:
| List | Subscribe |
|------|----------|
| Conspiracy content | https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FGloomyD%2Fblocklists%2Frefs%2Fheads%2Fmain%2Fdist%2Fcomplotistes.ublacklist.txt |
| AI-generated content (AI Slop / SEO) | https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FGloomyD%2Fblocklists%2Frefs%2Fheads%2Fmain%2Fdist%2Fia-seo.ublacklist.txt |
| Foreign interference (Viginum) | https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FGloomyD%2Fblocklists%2Frefs%2Fheads%2Fmain%2Fdist%2Fingerences.ublacklist.txt |

#### Foreign interference (Viginum)

This list includes domain names referenced in publicly available technical reports
published by Viginum (Service de vigilance et de protection contre les ingérences numériques étrangères),
as well as additional manually curated entries.

Viginum is a French public service operating under the authority of the Prime Minister,
responsible for identifying and analyzing foreign digital interference activities.

Sources:
- Official publications: https://www.sgdsn.gouv.fr/publications/rapports-de-viginum
- Official GitHub repository: https://github.com/VIGINUM-FR

This repository republishes domain names extracted from public documents for filtering purposes.
No claim is made regarding the legal status or intent of the referenced domains.



## Methodology

Lists are built from:

- Public institutional reports
- Manual review and monitoring
- Domain normalization and deduplication
- Automated generation via build script

Exports:

- `.nextdns.txt` → raw domains (one per line)
- `.ublacklist.txt` → uBlacklist rules with metadata header

---

## Disclaimer

These lists are provided for personal filtering purposes.

They reflect a curation policy aimed at reducing exposure to low-quality or manipulative content.  
Users remain responsible for how they apply these filters.


---

## 🇫🇷 Français

### À quoi sert ce dépôt ?
Certains sites diffusent des contenus trompeurs, de mauvaise qualité (générés par IA, « AI Slop »), ou des fausses informations, parfois à des fins politiques.
Ce projet propose des listes de blocage compatibles avec :

- **uBlacklist**
- **NextDNS**

Il est maintenu depuis la **France** et inclut des sources relatives à la surveillance des ingérences numériques en **Europe**.


### Outils compatibles
- **uBlacklist** : Extension navigateur (Chrome, Firefox, Safari) qui filtre les résultats de recherche Google.
  [Site officiel](https://ublacklist.github.io/)
- **NextDNS** : Résolveur DNS qui bloque traqueurs, publicités et contenus indésirables au niveau du réseau.
  [Site officiel](https://nextdns.io/?from=zjmur6v8)

### Comment utiliser ces listes ?
Vous pouvez :
- Ajouter manuellement les sites à bloquer
- Vous abonner aux listes publiques de filtres (voir ci-dessus)
- Copier-coller des listes depuis ce dépôt

## 🔐 Utilisation avec NextDNS

Les listes destinées à NextDNS sont disponibles dans le dossier `dist/` du dépôt.

Fichiers :
- `dist/complotistes.nextdns.txt`
- `dist/ia-seo.nextdns.txt`
- `dist/ingerences.nextdns.txt`

Chaque fichier contient un domaine par ligne et est destiné à être utilisé comme liste de blocage.

Pour les utiliser dans NextDNS :

1. Ouvrez votre configuration NextDNS.
2. Allez dans la section **Denylist**.
3. Copiez-collez les domaines depuis le fichier `.nextdns.txt` correspondant.

## Utilisation avec uBlacklist :
 | Nom de la liste                     | Lien d'abonnement                                                                                     |
 |-------------------------------------|------------------------------------------------------------------------------------------------------|
 | Contenus complotistes               | [S'abonner](https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FGloomyD%2Fblocklists%2Frefs%2Fheads%2Fmain%2Fdist%2Fcomplotistes.ublacklist.txt) |
 | Contenus générés par IA (SEO)       | [S'abonner](https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FGloomyD%2Fblocklists%2Frefs%2Fheads%2Fmain%2Fdist%2Fia-seo.ublacklist.txt) |
 | Ingérences étrangères (source Viginum) | [S'abonner](https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FGloomyD%2Fblocklists%2Frefs%2Fheads%2Fmain%2Fdist%2Fingerences.ublacklist.txt) |

#### Ingérences étrangères (Viginum)

Cette liste inclut des noms de domaine mentionnés dans des rapports techniques publics
publiés par Viginum (Service de vigilance et de protection contre les ingérences numériques étrangères), ainsi que des ajouts issus d’une veille manuelle.

Viginum est un service de l’État français placé sous l’autorité du Premier ministre,
chargé d’identifier et d’analyser les opérations d’ingérences numériques étrangères.

Sources :
- Publications officielles : https://www.sgdsn.gouv.fr/publications/rapports-de-viginum
- Dépôt GitHub officiel : https://github.com/VIGINUM-FR


Autre travail utilisé, celui des chercheurs de l'IRSEM sur les ingérences chinoises dans le monde (Baybridge) via des agences de communications spécialisées pour diffuser des informations sur un réseau de sites liés à ces agences et usurpant l'identité de sites locaux.

- Rapport officiel : https://www.irsem.fr/focus.html
- Dépôt GitHub officiel : https://github.com/PaulGCharon/BayBridge

Ce dépôt republie des noms de domaine extraits de documents publics à des fins de filtrage.
Aucune qualification juridique n’est portée sur les domaines référencés.





## Avertissement

Ces listes sont fournies à des fins de filtrage personnel.

Chaque utilisateur reste responsable de l’usage qu’il en fait.



## 🔎 Autres projets susceptibles de vous intéresser

### 📰 Next.ink – Détection de sites générés par IA

[Next.ink](https://next.ink/173214/recap-nous-avons-decouvert-des-milliers-de-sites-dinfo-generes-par-ia-tous-nos-articles/) publie une extension navigateur (Firefox & Chrome) permettant d’identifier des sites probablement générés massivement par des outils d’IA générative.

Leur travail remarquable recense plusieurs dizaines de milliers de sites générés par IA via une analyse à grande échelle.

[Télécharger leur extension sur Firefox](https://addons.mozilla.org/fr/firefox/addon/alerte-sur-les-sites-genai/)
[Télécharger leur extension sur Chrome](https://chromewebstore.google.com/detail/alerte-sur-les-sites-gena/bcmpghnhminmlljeomngepamejbopffc?authuser=0&hl=fr)


L’extension n’étant pas disponible sur Safari ou mobile, l’utilisation combinée de **uBlacklist** et **NextDNS** permet d’étendre le filtrage à davantage d’environnements, sans prétendre égaler la profondeur de leur analyse.

---

### 🚩 Red Flag Domains – Veille sur les dépôts suspects en .fr et .re

[Red Flag Domains](https://red.flag.domains/) propose une veille quotidienne des noms de domaine suspects nouvellement enregistrés sous les extensions françaises (.fr) et réunionnaises (.re).

Leur travail est directement intégré dans NextDNS et leurs données sont publiées en open source.

Ce projet contribue à une détection préventive des enregistrements de domaines potentiellement malveillants.