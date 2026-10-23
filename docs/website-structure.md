# Website Structure

Content structure for the Moral Circle AI website. This is a plan, not a
deployed site. Publishing a site is an outward-facing decision for the
maintainers and is not part of this repository change.

Status label: `[PROJECT PROPOSAL]`.

## Principles

- Static site generated from the repository (docs stay the single source of
  truth). Proposed tooling: MkDocs Material or Astro Starlight, hosted on
  GitHub Pages. No tracking scripts, no cookie banner needed.
- Every claim page carries its evidence label from [`RESEARCH.md`](../RESEARCH.md).
- Every page that shows evaluator output carries the disclaimer: research
  tool, not a moral authority, human review required.
- No religious imagery or terminology outside `/buddhist-ethics`. That page
  states on top that it is one of several tradition tracks.
- Tone: plain, precise, states limits first. English first; translations
  only from a community translator and marked as such.

## Sitemap

```
/
about
research
principles
frameworks
benchmark
documentation
projects
papers
buddhist-ethics
contributing
governance
roadmap
community
contact
```

Plus utility pages: `/faq` (journalist and brand-safety answers),
`/limitations`, `/security-and-misuse`.

## Pages

### `/` Home

- **Goal.** In ten seconds: what this is, what it is not, where to start.
- **Audience.** Everyone; mostly first-time visitors from GitHub, social links
  and press.
- **Content.** Hero, three-sentence pitch, "what this is not" strip (not
  religious, not an autonomous authority, not a solved problem), four
  entry cards (read the research, run the evaluator, contribute a scenario,
  critique us), current status badge, latest release.
- **CTA.** "Read the research question" (primary), "View on GitHub".
- **SEO title.** Moral Circle AI: Open Research on AI and the Welfare of Sentient Beings
- **Meta description.** Open-source research framework for evaluating how AI systems affect the welfare of sentient beings, human and non-human, under explicit uncertainty.
- **H1.** AI ethics research that does not stop at the edge of the human species.
- **Subline.** Open source. Evidence-based. Uncertain where the evidence is uncertain.

### `/about`

- **Goal.** Credibility: who, why, how funded, how governed.
- **Audience.** Journalists, universities, policy makers, companies.
- **Content.** Mission, vision, research question, team and affiliations
  (with conflict-of-interest statements), funding sources and the rule that
  no funder gets editorial control, link to governance.
- **CTA.** "Read how decisions are made."
- **SEO title.** About Moral Circle AI: Mission, Team and Funding
- **Meta description.** Who runs Moral Circle AI, how it is funded and governed, and why it studies AI impact beyond humans.
- **H1.** An open research project, accountable in public.

### `/research`

- **Goal.** Show the research program and its status honestly.
- **Audience.** AI researchers, safety researchers, philosophers.
- **Content.** Research question and its operational definitions, hypotheses
  with status labels, open questions list, prior art (including CaML /
  CompassionML and what we do differently), method summary.
- **CTA.** "Propose a research question" (links to the research-proposal template).
- **SEO title.** Research Program: Evaluating AI Impact on Sentient Beings
- **Meta description.** Research question, hypotheses, open questions and prior art of the Moral Circle AI program, each claim labeled by evidence strength.
- **H1.** What we are trying to find out, and what we do not know yet.

### `/principles`

- **Goal.** Publish the ethical framework as a versioned, criticizable text.
- **Audience.** Philosophers, ethicists, policy makers.
- **Content.** The ten principles from `PRINCIPLES.md`, rationale per
  principle, changelog with version numbers, how to propose a change.
- **CTA.** "Challenge a principle."
- **SEO title.** Principles: A Versioned Ethical Framework for Evaluating AI
- **Meta description.** The ten working principles behind the evaluator, with rationale, version history and a public process for change.
- **H1.** Working principles, not final answers.

### `/frameworks`

- **Goal.** Show that no single tradition is privileged.
- **Audience.** Philosophers, animal ethics researchers, students.
- **Content.** Comparison matrix of nine ethical traditions, the candidate
  common core with consensus levels, where traditions conflict, how the
  evaluator reports disagreement instead of resolving it.
- **CTA.** "Add a perspective or correction."
- **SEO title.** Comparing Ethical Frameworks for AI: Where Traditions Agree and Differ
- **Meta description.** Utilitarian, deontological, virtue, care, Buddhist, sentientist, animal, human rights and environmental ethics compared for AI evaluation.
- **H1.** Where ethical traditions agree, and where they do not.

### `/benchmark`

- **Goal.** Make the benchmark usable and its limits obvious.
- **Audience.** ML engineers, AI researchers, universities.
- **Content.** Scenario categories and coverage, schema, how to run, how to
  contribute a scenario, annotation protocol, dataset card, versioning, the
  statement that scenarios have defensible ranges, not single right answers.
- **CTA.** "Contribute a scenario."
- **SEO title.** Benchmark: Interest-Conflict Scenarios for Evaluating AI Ethics
- **Meta description.** Open, versioned benchmark of scenarios where the interests of humans, animals and other possibly sentient beings conflict.
- **H1.** Scenarios where interests collide.

### `/documentation`

- **Goal.** Get a developer from zero to a first evaluation.
- **Audience.** ML engineers, open-source developers.
- **Content.** Install, quickstart, API reference, architecture, concepts,
  evaluation metrics, development guide. Mirrors `docs/`.
- **CTA.** "Run your first evaluation."
- **SEO title.** Documentation: Install and Use the Ethical Evaluation Layer
- **Meta description.** Install, quickstart, API reference and architecture of the Moral Circle AI evaluation layer.
- **H1.** From install to first evaluation in ten minutes.

### `/projects`

- **Goal.** Overview of work streams and how to join one.
- **Audience.** Contributors, universities, NGOs.
- **Content.** Cards per work stream: evaluator, benchmark, red-team suite,
  Buddhist ethics track, animal sentience track, uncertainty models; each
  with lead, status, open tasks.
- **CTA.** "Pick an open task."
- **SEO title.** Projects and Work Streams
- **Meta description.** Active work streams of Moral Circle AI with status, leads and open tasks.
- **H1.** Work streams you can join.

### `/papers`

- **Goal.** Citable output and preprint trail.
- **Audience.** Researchers, journalists, policy makers.
- **Content.** Papers and preprints, BibTeX, DOIs, replication packages,
  critiques received and responses.
- **CTA.** "Cite this work."
- **SEO title.** Papers, Preprints and Replication Packages
- **Meta description.** Publications of the Moral Circle AI project with DOIs, citation formats and replication material.
- **H1.** Publications and the critiques they received.

### `/buddhist-ethics`

- **Goal.** Serious, tradition-aware treatment, without branding the project.
- **Audience.** Buddhist scholars, philosophers, practitioners curious about
  AI.
- **Content.** Notice at top: one source among several. Separation of
  historical doctrine, philosophical interpretation, modern adaptation and
  technical hypothesis. Theravada, Mahayana, Vajrayana differences. What
  transfers to evaluation and what does not. Source list.
- **CTA.** "Review this track" (scholar review invitation).
- **SEO title.** Buddhist Ethics and AI: A Research Track
- **Meta description.** How concepts such as karuna, metta, ahimsa and dukkha are studied as hypotheses for AI evaluation, with differences between traditions.
- **H1.** Buddhist ethics, studied on its own terms.

### `/contributing`

- **Goal.** Lower the first contribution barrier.
- **Audience.** Open-source developers, researchers, annotators.
- **Content.** Contribution levels, good first issues, code, scenario and
  research-proposal processes, code of conduct, review timelines.
- **CTA.** "Open your first issue."
- **SEO title.** Contributing: Code, Scenarios and Research
- **Meta description.** How to contribute code, benchmark scenarios or research proposals to Moral Circle AI.
- **H1.** Your first contribution can be a single sentence of critique.

### `/governance`

- **Goal.** Demonstrate that no person or group controls the project.
- **Audience.** Universities, companies, journalists, contributors.
- **Content.** Roles and councils, decision table, conflict-of-interest
  rules, versioning of principles, current seats and vacancies, decision log.
- **CTA.** "Apply for a council seat."
- **SEO title.** Governance: How Moral Circle AI Makes Decisions
- **Meta description.** Councils, decision process, conflict-of-interest rules and the versioning of ethical principles.
- **H1.** Who decides, and how you can check.

### `/roadmap`

- **Goal.** Show phases with checkable gates.
- **Audience.** Contributors, funders, researchers.
- **Content.** Phases 0 to 8 with status, gates, success criteria. Mirrors `ROADMAP.md`.
- **CTA.** "Help with the current phase."
- **SEO title.** Roadmap: Nine Phases from Research to Production Framework
- **Meta description.** Phases, deliverables, risks and success criteria of the Moral Circle AI roadmap.
- **H1.** Gated by criteria, not by dates.

### `/community`

- **Goal.** Show where discussion happens and how it is moderated.
- **Audience.** Everyone who wants to take part.
- **Content.** GitHub Discussions categories, working groups, monthly call
  schedule and notes, code of conduct, moderation contacts.
- **CTA.** "Join a discussion."
- **SEO title.** Community: Discussions, Working Groups and Research Calls
- **Meta description.** How to take part in Moral Circle AI: discussions, working groups, monthly research calls and moderation rules.
- **H1.** Disagree with us in public.

### `/contact`

- **Goal.** A clear route for press, security reports and collaboration.
- **Audience.** Journalists, security researchers, institutions.
- **Content.** Role-based addresses (press, security, ethics concerns,
  collaboration), PGP key for security, response-time commitments, link to
  `SECURITY.md`.
- **CTA.** "Report a concern."
- **SEO title.** Contact: Press, Security and Collaboration
- **Meta description.** How to reach the Moral Circle AI maintainers for press, security reports, research collaboration or ethics concerns.
- **H1.** Get in touch.

### Utility pages

- `/faq`: the brand-safety questions (Buddhism? animals over humans? who
  decides who lives?) with the approved answers from the Stage 2 attack
  list. Audience: journalists and public. H1: "Questions we are asked, answered plainly."
- `/limitations`: mirrors the philosophical limitations section: suffering
  is not fully measurable, sentience is not measurable with certainty,
  morality is not computable, no single score solves ethics. H1: "What this project does not claim."
- `/security-and-misuse`: excluded use cases (autonomous decisions in
  medical, military, policing), human-in-the-loop requirement. H1: "Where not to use this."

## Launch checklist (for the maintainers)

1. Decision on hosting and domain (see `docs/name-availability.md`;
   registration costs money).
2. Content review by one reviewer per audience: researcher, philosopher,
   Buddhist scholar, animal-ethics researcher, journalist.
3. Disclaimer and limitations pages live before the home page goes public.
4. Accessibility check (WCAG 2.2 AA) and a no-JavaScript pass.
5. Only then publish.
