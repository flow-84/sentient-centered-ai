# Stage 2: Projektdefinition & Marke v0.1

Research-Quality-Tags wie im Dossier: `[ESTABLISHED] [SUPPORTED] [HYPOTHESIS] [INTERPRETATION] [OPEN QUESTION] [CONTROVERSIAL] [PROJECT PROPOSAL]`. Grundlage: Research Dossier v0.1 (Stage 1, MS-603, Attachment `research-dossier-stage1.md`). Zwei ergaenzende Live-Funde aus dieser Stage, die das Dossier nicht kannte, sind unten markiert `[STAGE-2 FINDING]`.

---

## 1. Forschungsfrage (Master-Prompt Abschnitt 2)

### 1.1 Kritik der Ausgangsformulierung

> "Can artificial intelligence be designed and evaluated to systematically minimize unnecessary suffering and consider the well-being of sentient beings?"

Schwaechen:
- **"systematically minimize"** suggeriert einen loesbaren Optimierungsprozess. Das Dossier zeigt: Valenz ist "ill-defined and poorly operationalized" (Lindquist et al. 2023), es gibt keine Konsenstheorie von Bewusstsein (Cogitate Consortium, Nature 2025), und Delphi (2021) demonstriert die Gefahr, ein ungeloestes Messproblem als geloest zu behandeln. Die Formulierung impliziert eine Praezision, die die zugrunde liegende Wissenschaft nicht hergibt [OPEN QUESTION].
- **"artificial intelligence"** ist zu breit — das Projekt evaluiert konkrete Systeme (LLM-Outputs, Agentenentscheidungen), nicht "AI" als Abstraktum.
- **"unnecessary suffering"** enthaelt bereits eine normative Vorentscheidung (dass manches Leiden noetig ist), die operationalisiert werden muss, nicht vorausgesetzt werden darf.
- Die Frage ist rein technisch formuliert und verliert den Forschungscharakter (ob ueberhaupt, nicht nur wie).

### 1.2 Begriffsklaerung

| Begriff | Arbeitsdefinition | Quelle | Tag |
|---|---|---|---|
| **Sentient** | Faehigkeit zu valenzierten (positiv/negativ gefaerbten) Erfahrungen (Birch 2024) | Dossier, Sentience-Abschnitt | [PROJECT PROPOSAL, uses Birch's definition] |
| **Suffering** | Negativ valenzierte bewusste Erfahrung, von der das Subjekt motiviert ist, sie zu vermeiden/beenden; unterscheidet sich von reiner Nozizeption ohne Bewusstsein | Dossier | [ESTABLISHED distinction, unresolved measurement] |
| **Well-being** | Bilanz aus positiven und negativen Erfahrungen ueber Zeit (Ng 1995, "welfare biology") | Dossier | [ESTABLISHED definition, empirically schwer zu messen] |
| **Unnecessary suffering** | Leiden, das bei mindestens einer verfuegbaren Handlungsalternative mit vergleichbarem Nutzen vermeidbar gewesen waere — eine relationale, keine absolute Kategorie | Eigene Ableitung aus Moral-Uncertainty-Literatur (MacAskill et al. 2020) | [PROJECT PROPOSAL] |

**Operationalisierbarkeit:** Alle vier Begriffe sind nach Stand der Forschung graduell messbar (Konfidenzintervalle, Proxys, Verhaltensindikatoren), nicht binaer entscheidbar [ESTABLISHED, direkt aus Dossier]. Kein drittperspektivisches Verfahren kann Sentienz heute direkt nachweisen (Dossier, Abschnitt Sentience). Jede Operationalisierung des Projekts muss daher als **Schaetzung mit Konfidenz**, nicht als Tatsachenfeststellung, konstruiert sein — konsistent mit Birchs Vorsorgeprinzip und "Taking AI Welfare Seriously" (arXiv:2411.00986).

**Vermeidung unbegruendeter Sentienz-Zuschreibung:** Drei Leitplanken aus dem Dossier uebernommen: (1) verbale Selbstauskuenfte eines Systems ueber eigene Erfahrung sind keine verlaessliche Evidenz (Butlin et al. 2023); (2) Verhalten allein beweist kein Erleben (Valenz kann unbewusst wirken, Lindquist et al. 2023); (3) asymmetrische Vorsorge nach Birch: falsch-positive Sentienz-Annahme kostet unnoetige Einschraenkung, falsch-negative riskiert unentdecktes Leiden — die Kostenasymmetrie rechtfertigt Vorsicht, nicht Gewissheit.

### 1.3 Alternative Formulierungen

1. *"Can AI evaluation methods represent, rather than resolve, the moral uncertainty involved in weighing the interests of humans, non-human animals, and possibly artificial systems?"* — praezise, aber zu lang fuer eine Leitfrage.
2. *"What would it mean to design AI evaluation criteria that do not assume human interests are automatically privileged?"* — trifft den Kern, aber weniger konkret ueber Leiden/Wohlergehen.
3. *"Can open, testable methods be developed for identifying and weighing the welfare of sentient beings potentially affected by an AI system's outputs, under explicit uncertainty about sentience and consequences?"* — praezise, technisch anschlussfaehig, benennt Unsicherheit explizit.
4. *"Does AI ethics evaluation change materially when the scope of morally relevant interests is extended beyond humans, and can that extension be done without false certainty about sentience?"* — betont den Forschungscharakter (empirische Frage: aendert sich etwas), nicht nur normativ.

### 1.4 Empfehlung

**Gewaehlte Forschungsfrage:**

> "Can open, testable evaluation methods be developed that identify and represent the potential welfare impact of AI systems on all plausibly sentient beings affected by them, including explicit representation of uncertainty about sentience and consequences, without assuming that human interests are automatically privileged?"

Begruendung: erfuellt wissenschaftliche Praezision (nennt Methode, Messgegenstand, Unsicherheitsbehandlung), ist technisch umsetzbar (Evaluationsmethoden statt "die KI systematisch machen"), und ist oeffentlich verstaendlich in einer Kurzform reduzierbar (siehe Tagline unten). Sie beansprucht keine Loesung, sondern fragt nach Entwickelbarkeit — konsistent mit Rule 2 des Master-Prompts (keine unbelegten Behauptungen als Fakten). [PROJECT PROPOSAL]

Kurzform fuer Website/README: *"Can AI systems be evaluated for their impact on the welfare of all sentient beings they affect, not only humans, under honest uncertainty?"*

---

## 2. Projektname (Abschnitt 5)

### 2.1 Namenskandidaten-Recherche — Kollisionscheck

`[STAGE-2 FINDING]` Vor der Kandidatenliste: eine gezielte Web-Recherche zu den nahegelegten Namensraeumen ergab drei relevante Kollisionen, die das Research-Dossier (Stage 1) noch nicht kannte:

- **"Sentient" als Marke ist stark besetzt** im Krypto-/AI-Agenten-Raum: `sentient-agi` (Sentient AGI, Enclaves-Framework, Agent-Framework), `SentientAI` (GitHub-Org), mehrere unabhaengige "Sentient"-Repos. Ein Name mit "Sentient" als Kernbegriff waere leicht verwechselbar mit einem bestehenden Krypto-/Agenten-Oekosystem — hohe Verwechslungsgefahr, konkret gegen die Marken-Anforderung "wissenschaftliche Seriositaet, keine Verwechslungsgefahr".
- **"OpenSentience" existiert bereits** als aktives Projekt (opensentience.org, "Open Research into Machine Cognition", lokal-first Agent-Runtime) — direkte Namenskollision, nicht verwendbar.
- **"Compassion"/"CompassionML" (CaML)** ist eine bereits aktive Organisation ("Compassion Aligned Machine Learning", compassionml.com) mit Benchmarks fuer Tierwohl-Verhalten in KI (ANIMA, MORU, Manager Coercion Bench) und einer oeffentlichen Leaderboard (compassionbench.com) — inhaltlich der naechste bekannte Nachbar zum eigenen Vorhaben. Ein Name mit "Compassion" im Kern waere sowohl Kollisions- als auch Verwechslungsrisiko mit einer bereits etablierten Marke im selben Themenfeld.
- Zusaetzlich: "BenevolentAI" ist eine bestehende, boersennotierte britische Biotech-/KI-Firma — "Benevolent AI" als Name ist blockiert. "Moralis" ist eine etablierte Web3-Entwicklungsplattform — als Namensbestandteil ebenfalls blockiert. "Sentio" ist als Marken- und Produktname mehrfach vergeben (Sentio Software mit US-Patent, mehrere GitHub-Sentio-Projekte).

**Konsequenz fuer die Kandidatenauswahl:** "Sentient", "Sentio", "OpenSentience", "Compassion(ate)", "Benevolent AI", "Moralis" werden als Namenskerne ausgeschlossen oder nur mit deutlichem Zusatz/Abgrenzung weitergefuehrt. Diese Kollisionspruefung ist eine Stichprobe (wenige gezielte Suchen), keine vollstaendige Trademark-Recherche — vor der finalen Registrierung (Stage 5: Repo-Setup) ist eine formale Domain-/GitHub-Verfuegbarkeits- und Markenpruefung fuer den gewaehlten Namen noch offen [OPEN — Verifikation steht aus, siehe Abschnitt 2.4].

### 2.2 Kandidatenliste (32 Namen)

| # | Name | Kategorie | Bewertung |
|---|---|---|---|
| 1 | Sentient-Centered AI Ethics | wissenschaftlich | Praezise, aber "Sentient" kollisionsbelastet (2.1). Nur als Untertitel/Beschreibung nutzbar, nicht als Markenkern. |
| 2 | Sentience-Informed AI | wissenschaftlich | Vermeidet Ueberanspruch von "centered" (impliziert nicht, dass Sentienz das einzige Kriterium ist), kein Kollisionsfund. |
| 3 | Moral Patienthood Initiative | wissenschaftlich | Fachbegriff aus SEP (Dossier), praezise aber sperrig fuer Laien. |
| 4 | Welfare-Aware Alignment | wissenschaftlich | Direkter Anschluss an Alignment-Forschung, evtl. zu eng auf "Alignment" verengt. |
| 5 | Cross-Sentient Ethics Initiative | wissenschaftlich | Ungewoehnlich, aber grammatikalisch schwerfaellig. |
| 6 | Sentience-Inclusive AI Research | wissenschaftlich | Korrekt, aber lang; gut als Beschreibungssatz, schwach als Marke. |
| 7 | Ethical Evaluation Layer | technisch | Exakte Systembeschreibung (siehe Architektur-Diagramm im Master-Prompt), aber als Projektname zu generisch/produktartig. |
| 8 | Harm Minimization Framework | technisch | Klar, aber "Framework" + "Minimization" wirkt wie ein Software-Package-Name, keine Marke. |
| 9 | MoralUncertainty.dev | technisch | Nischenzielgruppe (Entwickler), Domain-artiger Name, wenig ausbaufaehig fuer breitere Kommunikation. |
| 10 | WelfareEval | technisch | Kurz, technisch klar, geringe emotionale/philosophische Tiefe. |
| 11 | SentioScope | technisch | Kollidiert mit "Sentio"-Markenfamilie (2.1) — verworfen. |
| 12 | EthicOS | technisch | Klingt nach Betriebssystem, mehrdeutig; geringe Unterscheidbarkeit. |
| 13 | Common Ethical Core | philosophisch | Direkter Bezug zu Abschnitt 19 des Master-Prompts (Common Ethical Core); klar, aber beansprucht implizit ein geloestes Ergebnis statt eines offenen Forschungsprozesses. |
| 14 | Moral Circle AI | philosophisch | Bezug auf etablierten SEP-/Singer-Begriff "moral circle" (Dossier). Wissenschaftlich verankert, nicht religioes, gut uebersetzbar, kein Kollisionsfund. |
| 15 | Karuna Alignment | philosophisch | Buddhistischer Fachbegriff im Markenkern — verletzt explizit die Markenstrategie-Vorgabe (nicht missionierend wirken) — verworfen. |
| 16 | Non-Harm AI | philosophisch | Klar, aber "non-harm" ist im AI-Safety-Feld bereits mit rein menschenzentrierten Harm-Kategorien besetzt (Dossier, EU-AI-Act-Abschnitt) — Verwechslungsgefahr mit bestehendem Safety-Vokabular. |
17 | Pluralist Ethics Lab | philosophisch | Betont Methodik (Abschnitt 11 im Dossier: Value Pluralism), "Lab" impliziert reine Forschungseinrichtung, weniger Community-Framework. |
| 18 | Beyond the Human Circle | philosophisch | Bildhaft, aber riskiert Fehllesung als "gegen den Menschen" (Brand-Safety-Risiko, siehe Abschnitt 4). |
| 19 | OpenSentience | Open Source | Direkte Namenskollision (2.1) — verworfen. |
| 20 | Open Compassion Framework | Open Source | Kollidiert konzeptionell mit CaML/CompassionML (2.1) — verworfen. |
| 21 | Open Moral Circle | Open Source | Kombiniert "Open Source"-Signal mit dem philosophisch verankerten Begriff; funktioniert, etwas laenger als Kandidat 14. |
| 22 | AI4Sentience | Open Source | Hashtag-artig, "4"-Schreibweise wirkt informell fuer ein wissenschaftliches Projekt. |
| 23 | Compassionate Intelligence | emotional | Kollisionsnahe zu CaML-Markenraum (2.1), zusaetzlich missverstaendlich als "emotionale KI" statt Ethik-Framework. |
| 24 | Benevolent AI | emotional | Bestehende Firma (2.1) — verworfen. |
| 25 | Gentle Systems | emotional | Angenehm, aber zu vage — koennte jedes UX-freundliche Softwareprojekt sein. |
| 26 | Kinder AI | emotional | Wirkt kindlich/unseriös im Doppelsinn ("kinder" engl. auch "Kinder") — verworfen. |
| 27 | Considerate AI | emotional | Verstaendlich, warm, nicht religioes; Risiko: klingt nach Kundenservice-/Etikette-Tool statt Forschungsprojekt — nur mit klarer wissenschaftlicher Unterzeile tragfaehig. |
| 28 | Sentira | international | Kunstwort, international aussprechbar, aber ohne erkennbaren Begriffsanker — erklaerungsbeduerftig. |
| 29 | Compassio | international | Lateinischer Wortstamm von "Compassion" — bleibt im Kollisionsradius von CaML (2.1). |
| 30 | Considera AI | international | Kunstwort-Variante von "considerate", international lesbar, kein Kollisionsfund. |
| 31 | Sentien | kurz/markenfaehig | Kurzform von "sentient" — bleibt im Kollisionsradius von "Sentient"-Markenfamilie (2.1), da phonetisch sehr nah. |
| 32 | Wellsentient | kurz/markenfaehig | Kombiniert "well-being" + "sentient", neu, aber Aussprache/Lesbarkeit im internationalen Kontext unsicher. |

### 2.3 Empfehlung

**Hauptname: Moral Circle AI**

Begruendung gegen die Pruefkriterien:
- **Bedeutung**: direkter, im Dossier belegter Fachbegriff (Lecky 1869, Singer 1981, SEP) fuer genau die Forschungsfrage des Projekts — Ausweitung des Kreises moralisch beruecksichtigter Wesen.
- **Aussprache/internationale Verstaendlichkeit**: einfache englische Woerter, keine Sonderzeichen, in D-A-CH wie international aussprechbar.
- **Verwechslungsgefahr**: in der gezielten Recherche (2.1) kein kollidierendes Projekt gefunden — Restrisiko bleibt, da keine vollstaendige Trademark-Datenbank-Pruefung erfolgte [OPEN QUESTION, siehe 2.4].
- **Religioese/politische Konnotation**: keine — "moral circle" ist ein saekularer philosophischer Fachbegriff, nicht buddhistisch, nicht politisch codiert.
- **Wissenschaftliche/technische Seriositaet**: hoch, da direkt aus der akademischen Literatur (SEP-Eintrag "The Moral Status of Animals" u.a.) abgeleitet, nicht erfunden.
- **Markenfaehigkeit/Domain/GitHub-Potenzial**: kurze zwei-Wort-Kombination + "AI"-Suffix, gut merkbar; konkrete Domain (`moralcircle.ai` / `.org`) und GitHub-Verfuegbarkeit sind vor Registrierung technisch zu pruefen (Stage 5) [OPEN].
- **Negative Interpretierbarkeit**: gering — anders als z. B. "Beyond the Human Circle" impliziert der Name keine Anti-Human-Position, sondern eine Erweiterung, was fuer die Markenstrategie (Abschnitt 22/3 unten) zentral ist.

**Alternativen (in Prioritaetsreihenfolge):**
1. **Sentience-Informed AI** — konservativer, noch staerker wissenschaftlich-zurueckhaltend formuliert (impliziert keine feste Position, nur "informiert durch" Sentienzforschung); guter Fallback, falls "Moral Circle" bei formaler Pruefung Kollisionen zeigt.
2. **Considerate AI** — zugaenglicher, staerker fuer allgemeine Oeffentlichkeit/Journalisten geeignet; Risiko der Verwechslung mit Etikette-/UX-Tools muesste durch klare Unterzeile ("An open research framework for...") abgefangen werden.
3. **Open Moral Circle** — identisch verankert wie der Hauptname, betont zusaetzlich explizit den Open-Source-Charakter; guter Kandidat, falls "Moral Circle AI" als Domain/GitHub-Organisation nicht verfuegbar ist.

### 2.4 Offener Punkt

Formale Verfuegbarkeitspruefung (Domain-Registrare, GitHub-Organisationsname, USPTO/EUIPO-Markendatenbank-Stichprobe) fuer "Moral Circle AI" und die drei Alternativen ist **nicht** Teil dieser Stage und noch nicht durchgefuehrt — naechster Schritt: vor der Repo-Erstellung in Stage 5 (MS-607, aktuell aber laut Board bereits `in_review` — dort gegenpruefen, ob ein Name bereits verbaut wurde, bevor diese Empfehlung uebernommen wird).

---

## 3. Markenstrategie (Abschnitt 6)

| Element | Text |
|---|---|
| **Name** | Moral Circle AI |
| **Tagline** | Open research on evaluating AI's impact on every sentient being it affects. |
| **Mission** | Moral Circle AI develops and tests open methods for evaluating how AI systems affect the welfare of sentient beings, human and non-human, under explicit uncertainty rather than false certainty. |
| **Vision** | A future in which the potential impact of an AI system on affected sentient beings is considered during design, not only after deployment, and in which that consideration is open to scientific scrutiny rather than asserted by authority. |
| **One-liner** | An open-source research framework for evaluating AI systems' impact on the welfare of all plausibly sentient beings they affect. |
| **Elevator Pitch** | Most AI ethics frameworks evaluate systems only by their impact on humans. Moral Circle AI is an open, interdisciplinary research project building testable methods, benchmarks, and an evaluation layer that account for the welfare of non-human animals and other sentient beings too, while being explicit about what remains scientifically uncertain. We are not claiming to have solved ethics. We are building tools to study it rigorously and pluralistically, in the open. |
| **Website Hero Text** | AI ethics research that does not stop at the edge of the human species. Open source. Evidence-based. Uncertain where the evidence is uncertain. |
| **GitHub Description** | Open research framework for evaluating AI systems' impact on the welfare of sentient beings, human and non-human, under explicit moral and scientific uncertainty. |
| **Social Media Bio** | Open-source AI ethics research. Evaluating impact on all sentient beings an AI system affects, not only humans. Science first, no dogma. |
| **Wissenschaftliche Kurzbeschreibung** | An interdisciplinary open-source research project developing testable evaluation methods, benchmarks, and an ethical-evaluation-layer prototype for assessing AI systems' potential harm to and welfare impact on sentient beings, extending beyond the predominantly anthropocentric scope of existing AI ethics, alignment, and governance frameworks (UNESCO 2021, EU AI Act 2024, OECD AI Principles 2024), while explicitly representing scientific and moral uncertainty rather than resolving it by assumption. |

Abgrenzung zur Markenstrategie-Vorgabe (Master-Prompt Abschnitt 6): kein Element oben nennt Buddhismus, keine religioese Terminologie, keine veganistische/politische Positionierung. "Compassion", "non-harm" und "pluralism" als Werte sind in Mission/Vision sprachlich vorhanden, aber nicht namensbildend — sie werden inhaltlich (Abschnitt 4 unten) statt markenwoertlich transportiert, um die in 2.1 identifizierte Kollision mit CaML/CompassionML zu vermeiden.

---

## 4. Mission & Vision — vertieft (Abschnitte 7 & 8)

**Mission (Langform):** Moral Circle AI erforscht und entwickelt offene, ueberpruefbare Methoden, um zu bewerten, wie KI-Systeme das Wohlergehen betroffener empfindungsfaehiger Wesen beeinflussen — einschliesslich, aber nicht beschraenkt auf Menschen. Das Projekt behauptet nicht, moralische Wahrheit zu besitzen oder Sentienz zuverlaessig messen zu koennen. Es behauptet, dass die Frage, wessen Interessen zaehlen, bislang in der etablierten AI-Ethics-/Alignment-/Governance-Literatur kaum systematisch gestellt wird (Dossier, Cross-Cutting Synthesis Punkt 1) — und dass diese Luecke offene, wissenschaftlich fundierte Forschung verdient, keine stillschweigende Fortschreibung des Status quo.

**Vision (Langform):** Eine Zukunft, in der ethische Folgenabschaetzung fuer KI-Systeme so selbstverstaendlich zum Entwicklungsprozess gehoert wie Sicherheits- oder Datenschutzpruefungen — und in der diese Folgenabschaetzung den Kreis der beruecksichtigten Interessen nicht per Voreinstellung auf Menschen begrenzt. Diese Vision behauptet nicht, dass Tiere, Oekosysteme oder zukuenftige kuenstliche Systeme tatsaechlich moralisch gleichwertig mit Menschen sind — sie behauptet nur, dass diese Frage eine ernsthafte, wissenschaftlich gefuehrte Pruefung verdient statt einer unbegruendeten Verneinung per Default.

Beide Formulierungen folgen explizit "wir erforschen und entwickeln" statt "wir besitzen die moralische Wahrheit" (Master-Prompt-Vorgabe Abschnitt 7).

---

## 5. Brand Safety — Angriffe & Antworten (Abschnitt 22)

Format je Eintrag: **Angriff** → *Antwort* (Tag zur Einordnung des Angriffstyps).

1. **"Das ist einfach Buddhismus als KI-Moral."** → *Buddhist ethics is one of several philosophical traditions we study alongside utilitarianism, deontology, care ethics, and others (see Dossier Section 3). No tradition is treated as the project's answer.* (religioes)
2. **"Ihr bevorzugt Tiere gegenueber Menschen."** → *We do not prescribe a predetermined hierarchy between species. We study how competing interests can be evaluated under uncertainty — see our Human Safety Principle, which explicitly keeps human rights and safety in scope.* (Speziesismus-Vorwurf)
3. **"Ihr behauptet, Tiere seien genauso moralisch relevant wie Menschen."** → *We investigate moral consideration based on plausible capacity for sentience, explicitly weighted by uncertainty. We do not assert equal moral weight; we study how weight should be assigned under evidence.* (Ueberinterpretation)
4. **"Ihr baut eine KI, die entscheidet, wer leben darf."** → *This is a research and evaluation framework, not an autonomous decision authority. Every design document states human-in-the-loop review for high-stakes use (see Level 9, Human Safety Principle).* (dystopische Zuspitzung)
5. **"Das ist Marketing-Woke-Ethik, keine echte Wissenschaft."** → *Every claim in our research materials is tagged by evidentiary status (established, supported, hypothesis, open question). Readers can verify sources directly; nothing is asserted without citation.* (politische Diskreditierung)
6. **"Ihr wollt Fleischkonsum verbieten."** → *The project makes no policy recommendations about diet, agriculture, or consumer behavior. It is an AI evaluation research framework, not an advocacy campaign.* (veganistische Unterstellung)
7. **"Wenn ihr nicht sicher seid, ob Tiere/KI leiden koennen, warum baut ihr dann darauf ein Projekt?"** → *Precisely because the uncertainty is real and consequential, we build methods to represent it explicitly rather than ignore it by default — the same logic UK law used to extend welfare protection to decapods under scientific uncertainty (Birch et al. 2021).* (Legitimationsangriff)
8. **"Das ist nur ein weiteres AI-Ethics-Vaporware-Projekt ohne echten Code."** → *The repository includes a working MVP evaluation prototype, a benchmark dataset, and reproducible tests from the first release; roadmap and current status are public.* (Substanzvorwurf)
9. **"Ihr wollt Menschen die Kontrolle ueber KI entziehen."** → *No principle in the framework removes human oversight. Human safety and rights remain an explicit, non-negotiable layer of every evaluation.* (Kontrollverlust-Angst)
10. **"Warum ausgerechnet 'sentient beings' und nicht Umwelt/Oekosysteme insgesamt?"** → *We scope to sentience because it is the criterion that links directly to suffering and welfare — interests that can be helped or harmed. We document this as a deliberate scope choice, not a claim that ecosystems don't matter (see biocentrism comparison in our ethics-comparison matrix).* (Scope-Kritik)
11. **"Das klingt esoterisch/pseudowissenschaftlich."** → *Every technical and philosophical claim is source-tagged against peer-reviewed literature; speculative claims are explicitly labeled as hypotheses, not findings.* (Seriositaets-Angriff)
12. **"Ihr instrumentalisiert Buddhismus fuer PR."** → *Buddhist ethics is credited as one documented source of hypotheses (karuna, ahimsa) among many, cited with named scholars and primary texts, not used as branding or imagery.* (kulturelle Aneignung)
13. **"Das ist doch nur Silicon-Valley-Effektiver-Altruismus in neuem Anstrich."** → *We cite EA-adjacent work (e.g. Sentience Institute) as one input among many and explicitly flag its advocacy framing as distinct from our own neutral research stance; our governance is independent of any single movement or funder.* (Bewegungs-Vereinnahmung)
14. **"Niemand kann Leiden objektiv messen, also ist das ganze Projekt unwissenschaftlich."** → *Correct that no direct third-person measurement of suffering exists today — which is why the framework represents welfare as a confidence-weighted estimate, not a claimed objective score (see Uncertainty Principle).* (Messbarkeits-Einwand)
15. **"Das Projekt wird von Big Tech gekapert, um sich ein gruenes Ethik-Mäntelchen umzuhaengen."** → *Governance separates the Ethics Council from any single corporate funder; changes to the ethical core require documented multi-stakeholder review, published in the open (see Governance).* (Vereinnahmungs-Risiko)
16. **"Ihr wollt KI Rechte geben."** → *The project studies whether some future AI systems could warrant moral consideration if evidence of sentience emerges; it makes no legal-rights claim and no claim about current systems.* (Rechte-Fehlinterpretation)
17. **"Das ist Anthropomorphismus — ihr behandelt Software wie ein Lebewesen."** → *The framework explicitly states there is no scientific consensus that any current AI system is sentient (Chalmers 2023); this is a stated open research question, not an assumption.* (Anthropomorphismus-Vorwurf)
18. **"Wenn ihr unsicher seid, warum behauptet ihr dann irgendetwas?"** → *We distinguish established findings from hypotheses throughout (see our Research Quality Standard); the project's contribution is method and infrastructure, not moral certainty.* (Nihilismus-Einwand)
19. **"Das ist nur ein Rebranding von Effective Altruism/Longtermism."** → *We do not adopt longtermist prioritization frameworks or existential-risk arguments; our scope is present and near-term AI systems' welfare impact, evaluated empirically.* (ideologische Zuordnung)
20. **"Ihr wollt eine globale Ethik-Behoerde fuer KI werden."** → *The project has no enforcement authority and seeks none; outputs are research artifacts (benchmarks, evaluation tools) that any developer may use, ignore, or critique.* (Machtanspruch-Vorwurf)
21. **"Warum vertraut ihr LLM-as-judge fuer ethische Bewertungen — das ist doch zirkulaer."** → *We document this exact risk (see RLAIF/LLM-as-judge limitations in our architecture notes) and require human-in-the-loop validation and adversarial red-teaming before any evaluator output is treated as reliable.* (Methodenkritik)
22. **"Ihr kopiert einfach Anthropics Constitutional AI."** → *Constitutional AI is credited as prior art we build on, not invented by us; our contribution is extending the scope of the constitution to non-human welfare and adding explicit moral-uncertainty representation, which Constitutional AI does not do.* (Originalitaets-Vorwurf)
23. **"Das Projekt ist zu akademisch, um praktisch relevant zu sein."** → *The MVP ships an API and a benchmark usable by any developer today; academic rigor and practical usability are treated as compatible, not opposed, goals.* (Praxisrelevanz-Zweifel)
24. **"Ihr verschweigt, dass Tierwohl-Forschung selbst hoechst umstritten ist."** → *We cite the contested status directly (e.g. moral-circle-expansion framing flagged as advocacy-adjacent and controversial in our own dossier); disagreement is documented, not hidden.* (Transparenz-Vorwurf)
25. **"Wieso engagiert ihr euch nicht einfach fuer Tierschutzgesetze statt fuer KI-Forschung?"** → *Different projects address different levers; we contribute AI-evaluation methodology specifically, and explicitly do not position ourselves as a policy-advocacy or lobbying organization.* (Scope-Verwechslung)
26. **"Das klingt wie eine Sekte mit wissenschaftlichem Anstrich."** → *Governance is public, contributions are open, no membership pledge or belief statement is required to contribute — the project is a research repository, not a community with doctrine.* (Sektenverdacht)
27. **"Wenn ihr Unsicherheit so betont, warum habt ihr dann ueberhaupt ein Ethical Framework mit 10 Prinzipien?"** → *The ten principles are a testable research proposal (explicitly labeled as such), not a claimed solution; each is open to revision through the documented governance process for changing the ethical core.* (Widerspruchs-Vorwurf)
28. **"Das ist reine Publicity fuer die Gruender."** → *All contributors, decisions, and funding sources are disclosed in the repository under Governance and Conflicts of Interest; no anonymous or undisclosed backing.* (Motivkritik)
29. **"Ihr instrumentalisiert Leiden von Tieren, um KI-Firmen ein gutes Gewissen zu verkaufen."** → *The project publishes primary evaluation findings openly, including negative results about specific systems; it does not offer certification, endorsement, or compliance seals for a fee.* (Greenwashing-Vorwurf)
30. **"Warum kein einzelner 'Ethik-Score' — das macht das Projekt praktisch nutzlos fuer Entscheidungen."** → *A single score was evaluated and explicitly rejected (see Ethical Impact Model, Section 11) because it hides trade-offs and invites Goodhart's-Law gaming, as Delphi's 2021 failure demonstrated; a multi-dimensional profile is the documented, evidence-based alternative.* (Nutzlosigkeits-Vorwurf)

---

## 6. Zielgruppen / Personas (Abschnitt 25)

| Persona | Problem | Interesse | Nutzen | Messaging | Einstiegspunkt |
|---|---|---|---|---|---|
| **AI Researchers** | Fehlende Non-Human-Perspektive in bestehenden Ethik-Benchmarks | Neue, wissenschaftlich fundierte Forschungsluecke | Zitierbare Methodik, Benchmark-Datensatz | "A documented gap in the literature, not a solved problem" | Research Dossier + Paper-Entwurf |
| **ML Engineers** | Brauchen praktikable Evaluationstools, keine Philosophie-Seminare | Konkrete API/Library zum Integrieren | Drop-in Ethical Evaluation Layer, Beispielcode | "One API call to get a multi-framework welfare assessment" | Quickstart/API-Doku |
| **AI Safety Researchers** | Safety-Literatur ist fast ausschliesslich menschenzentriert | Erweiterung des Safety-Scopes um Welfare-Harm-Kategorie | Neue Red-Teaming-Szenarien, Anti-Goodhart-Analysen | "Safety research that accounts for harms your current benchmarks don't measure" | Benchmark + Red-Team-Programm |
| **Philosophers** | Technische Projekte vereinfachen Ethik meist unzulaessig | Seriöse, differenzierte Operationalisierung philosophischer Konzepte | Vergleichsmatrix, offene Fragen sauber dokumentiert | "We tag every claim by evidentiary status — nothing is flattened into a score without caveat" | Vergleichsmatrix + Philosophy Track Docs |
| **Animal Ethics Researchers** | KI-Governance ignoriert Tierwohl fast vollstaendig | Konkreter technischer Hebel fuer ihr Forschungsfeld | Direkter Beitragskanal fuer Szenarien/Benchmarks | "The first open evaluation framework that treats animal welfare as in-scope, not an afterthought" | Benchmark-Contribution-Prozess |
| **Buddhist Scholars** | Sorge vor oberflaechlicher/instrumentalisierender Nutzung buddhistischer Konzepte | Seriöse, differenzierte Behandlung ihrer Tradition | Eigener Research Track mit Quellenangaben je Schule (Theravada/Mahayana/Vajrayana) | "Buddhist ethics studied on its own terms, not flattened into slogans" | Buddhist Ethics & AI Research Track |
| **Open Source Developers** | Viele AI-Ethics-Projekte sind Closed-Source oder reine Whitepaper | Mitmachbares, aktives Repository | Klare Contribution-Guidelines, gute Issue-Struktur | "A real, working repository — not a whitepaper" | CONTRIBUTING.md + Good-First-Issues |
| **AI Companies** | Regulatorischer/reputationeller Druck, Ethik nachweisbar zu machen | Externe, glaubwuerdige Evaluationsreferenz | Ethical Impact Assessment als optionales Zusatzverfahren | "An independent, open evaluation layer you can adopt or ignore — no certification fees, no lock-in" | API + Ethical Impact Assessment Docs |
| **Universities** | Suchen reproduzierbare Forschungsinfrastruktur fuer AI-Ethics-Kurse/Studien | Lehrmaterial, Benchmark fuer eigene Studien | Reproduzierbare Experimente, offene Datensaetze | "Built for reproducibility: every experiment ships with hypothesis, method, and failure conditions" | Research.md + Experiments |
| **NGOs** | Brauchen technisch fundierte Evidenz fuer Advocacy-Arbeit | Belastbare, nicht-advocacy-verzerrte Datenbasis | Zitierbare, neutrale Forschungsergebnisse | "Independent research, not advocacy — you can build your own case on top of it" | Published Findings/Papers |
| **Policy Makers** | Brauchen technisch informierte, aber verstaendliche Entscheidungsgrundlagen | Neutrale Evidenzbasis fuer Regulierung | Kurzfassungen, EIA-kompatible Methodik | "A research-grade complement to existing frameworks like the EU AI Act and UNESCO Recommendation, not a replacement" | Policy Brief (Stage 9) |
| **Journalists** | Suchen einordbare, nicht sensationalistische KI-Ethik-Geschichten | Verstaendliche, belegte Aussagen mit klaren Grenzen | Klare FAQ, Brand-Safety-Antworten als Interview-Grundlage | "We tell you what we don't know as clearly as what we do" | About + FAQ/Brand-Safety-Seite |
| **General Public** | Ueberforderung durch abstrakte KI-Ethik-Debatten | Verstaendliche Einordnung, ohne belehrt zu werden | Klare, undogmatische Erklaerstuecke | "AI ethics research that admits what it doesn't know yet" | Website Hero + Blog/Explainer |

---

## 7. Marketing & Community — Grundlagen (Abschnitte 26/27, Detailausarbeitung folgt in Stage 9)

**Marketing-Prioritaet:** wissenschaftliche Glaubwuerdigkeit vor Reichweite. Kanaele in Reihenfolge der Passung: GitHub (Code + Discussions), arXiv (Paper-Preprints), akademische Konferenzen/Workshops, Hugging Face (Datasets/Modelle), dann erst breitere Kanaele (X, LinkedIn, Reddit r/MachineLearning, Mastodon).

**Fuenf Campaign-Linien** (Ausfuehrung in Stage 9):
- Campaign A "AI Safety" — Anschluss an Safety-/Alignment-Communities, Fokus Red-Teaming/Benchmark.
- Campaign B "Buddhist Ethics & AI" — eigener, klar abgegrenzter Track fuer buddhistische Communities, ausdruecklich ohne Vereinnahmung der Hauptmarke (kein "Moral Circle AI ist buddhistisch").
- Campaign C "Animal Sentience" — Zielgruppe Animal-Ethics-Forschung/NGOs, Anschluss an Wild Animal Initiative/Sentience-Institute-Netzwerk als Interlocutors, nicht als Verbuendete mit gleicher Agenda.
- Campaign D "Open Source AI Ethics" — Entwickler-Community, Contribution-getrieben.
- Campaign E "Academic Research" — Paper, Konferenzen, Zitationsstrategie.

**Community-Grundstruktur:** GitHub Discussions als primaerer oeffentlicher Kanal (kein separates Discord/Matrix in der MVP-Phase, um Moderationsaufwand niedrig zu halten); monatlicher offener Research Call sobald >3 aktive externe Contributors; Contribution-Level-Abstufung (Issue-Kommentar → Benchmark-Szenario-PR → Code-PR → Research-Proposal) wird in Stage 9 vollstaendig ausgearbeitet.

---

## 8. Bindende Ergebnisse fuer Folge-Stages

- **Stage 5 (Repo-Setup, MS-607)**: Repo-/Org-Name **"Moral Circle AI"** (Fallback: Sentience-Informed AI / Considerate AI / Open Moral Circle), vorbehaltlich formaler Domain-/GitHub-/Marken-Verfuegbarkeitspruefung (offen, Abschnitt 2.4). MS-607 steht laut Board bereits auf `in_review` — vor Uebernahme dieser Empfehlung dort gegenpruefen, ob bereits ein anderer Name verbaut wurde.
- **Stage 7 (README)**: Tagline, Mission, Vision, One-liner, GitHub-Description, wissenschaftliche Kurzbeschreibung aus Abschnitt 3 sind copy-paste-fertig.
- **Stage 3 (Ethical Framework)**: `[STAGE-2 FINDING]` CaML/CompassionML (compassionml.com, Benchmarks ANIMA/MORU/Manager-Coercion-Bench, compassionbench.com) ist ein direkter inhaltlicher Nachbar, den das Stage-1-Dossier nicht kannte — sollte in der Prior-Art-Betrachtung von Stage 3/4 ergaenzt und zitiert werden, nicht uebersehen.
