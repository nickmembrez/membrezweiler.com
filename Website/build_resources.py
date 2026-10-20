#!/usr/bin/env python3
"""Generate teaching-resources.html from the lab metadata below."""
import html, os

LABS = [
    # (file, course_key, course_label, title, description)
    ("SOC1113_YouDrawIt.html", "intro", "Introduction to Sociology", "You Draw It",
     "Students sketch their prediction of a social trend on a blank axis before the real series is revealed, which turns a passive chart into a record of what they believed and how wrong it was."),
    ("SOC1113_HowToLieWithAChart.html", "intro", "Introduction to Sociology", "How to Lie with a Chart",
     "Real published data with controls that change only how it is drawn. The axis baseline, direction, and scale move; the numbers never do. Students see how far a presentation can be pushed without a single false value."),
    ("SOC1113_CensusCategories.html", "intro", "Introduction to Sociology", "Census Categories",
     "Every race and ethnicity option that has appeared on a United States census questionnaire since 1790, shown by year, so students can watch an official classification system change shape around the population it claims to count."),
    ("SOC1113_CultureCompare.html", "intro", "Introduction to Sociology", "Culture Compare",
     "Published cross-national survey measurements of cultural traits, including norm tightness and individualism, arranged so students can compare countries and interrogate what a national average can and cannot support."),
    ("SOC1113_SitesOfSocialization.html", "intro", "Introduction to Sociology", "Sites of Socialization",
     "Data on family, school, peers, media, and religion as agents of socialization, with the relative weight of each put in front of students rather than asserted."),
    ("SOC1113_FrontStage.html", "intro", "Introduction to Sociology", "Front Stage",
     "Goffman wrote about dinner parties and shop counters in 1959. This lab tests dramaturgical analysis against contemporary evidence about self-presentation and audience."),
    ("SOC1113_BestPractices.html", "intro", "Introduction to Sociology", "Best Practices",
     "A simulation of the rationalized workplace, in which students apply efficiency logic to a work process and confront what the resulting standardization does to the people inside it."),
    ("SOC1113_LaunchControl.html", "intro", "Introduction to Sociology", "Launch Control",
     "Why good organizations do bad things. Students work through an organizational decision in which no individual does anything obviously wrong and the outcome is a disaster anyway."),
    ("SOC1113_Schelling.html", "intro", "Introduction to Sociology", "The Schelling Segregation Model",
     "A runnable agent model in which nobody prefers segregation and every agent only wants not to be badly outnumbered on its own block. Students set the tolerance threshold and watch the neighborhood sort itself anyway."),
    ("SOC1113_WholePie.html", "intro", "Introduction to Sociology", "The Whole Pie, Guessed First",
     "Students guess the composition of American incarceration before seeing it, then compare their estimate against the published breakdown and consider what labeling theory predicts about who ends up counted."),
    ("SOC1113_LifeChances.html", "intro", "Introduction to Sociology", "Life Chances",
     "Weber's concept made measurable. Students trace how position at birth translates into differing probabilities across education, health, and income."),
    ("SOC1113_BornLucky.html", "intro", "Introduction to Sociology", "Born Lucky",
     "Nobody chooses where they start. An extended interactive treatment of ascribed position and the cumulative advantage that follows from it."),
    ("SOC1113_PayGap.html", "intro", "Introduction to Sociology", "The Pay Gap, Taken Apart",
     "The raw gender pay gap, then what survives when occupation, hours, and experience are held constant, then what is left over. Students take the number apart rather than accepting or dismissing it whole."),
    ("SOC1113_FamilyMeasured.html", "intro", "Introduction to Sociology", "The Family, Measured",
     "Marriage, divorce, how couples meet, the division of household labor, and the evidence on what family structure does and does not do to child outcomes."),
    ("SOC1113_Population.html", "intro", "Introduction to Sociology", "The Three Drivers",
     "Births, deaths, and migration, with the published series for each and the forecasts they add up to. Students build a population story from its three components."),
    ("SOC1113_TheMovement.html", "intro", "Introduction to Sociology", "The Movement",
     "How social change actually happens. Students work through the resources, framing, and political opportunity behind a movement rather than treating change as the result of sentiment."),

    ("SOC3333_PerceptionGap.html", "criminology", "Criminology", "The Perception Gap",
     "The distance between what Americans believe about crime and what crime data show. Students estimate first, then meet the measurements, then account for the gap."),
    ("SOC3333_WhatAreYouCounting.html", "criminology", "Criminology", "What Are You Counting?",
     "Every crime number was produced by an institution with a procedure. Students specify exactly what their chosen offense type consists of and find out how much of it any given system counts."),
    ("SOC3333_DarkFigure.html", "criminology", "Criminology", "The Dark Figure",
     "Where official crime data come from, how victimization surveys differ, and what neither one can see. The lab builds the funnel from incident to statistic step by step."),
    ("SOC3333_SortingCrime.html", "criminology", "Criminology", "Sorting Crime",
     "A typology is a filing system, and filing systems have consequences. Students sort real events into violent, property, and public order categories and discover the cases that break the scheme."),
    ("SOC3333_HarmGap.html", "criminology", "Criminology", "The Harm Gap",
     "Offenses that do not fit the machinery built for street crime: crime in suites, crime as enterprise, and crime that scales. Students compare harm against enforcement attention."),
    ("SOC3333_PatternTest.html", "criminology", "Criminology", "The Pattern Test",
     "Crime is patterned rather than random, and those regularities are the reason criminological theory exists. Students identify the patterns their theories will later have to explain."),
    ("SOC3333_Deterrence.html", "criminology", "Criminology", "Beccaria's Arithmetic",
     "Beccaria argued in 1764 that punishment should work like arithmetic. Students run the calculation under varying certainty, severity, and celerity, and find where the arithmetic stops predicting behavior."),
    ("SOC3333_CrimeSchool.html", "criminology", "Criminology", "Who Taught You That?",
     "Differential association against the chapter that came before it. If crime requires no teaching, only a failure of restraint, what work is left for a learning theory to do?"),
    ("SOC3333_ToldToWin.html", "criminology", "Criminology", "Told to Win",
     "Merton's nine-page 1938 argument, tested. American culture prescribes the same goal to everyone and distributes the means unequally. Students trace each adaptation through cases."),
    ("SOC3333_WhyDidntYou.html", "criminology", "Criminology", "Why Didn't You?",
     "Control theory refuses the standard question. Instead of asking why some people offend, it asks why most people do not, and students apply that inversion to their own restraint."),
    ("SOC3333_TheMark.html", "criminology", "Criminology", "The Mark",
     "Labeling theory and the field's third domain, which is the reaction to crime rather than its causes. Students follow what a criminal label does after it attaches."),
    ("SOC3333_CrimeTriangle.html", "criminology", "Criminology", "Three Things Have to Line Up",
     "Routine activity theory takes the offender as given and asks what else had to be true. Students manipulate offender, target, and guardianship and watch which combinations produce an event."),
    ("SOC3333_TheOtherHalf.html", "criminology", "Criminology", "The Other Half",
     "Victimization, taught with care. The lab presents the patterns and the measurement problems without asking any student to disclose anything about themselves."),
    ("SOC3333_WhatItBuys.html", "criminology", "Criminology", "What It Costs, What It Buys",
     "Five competing purposes of punishment that do not agree with each other. Students assign sentences, then discover which rationale their own choices actually served."),
    ("SOC3333_FixThePlace.html", "criminology", "Criminology", "Fix the Place",
     "Situational crime prevention changes the unit of analysis from the person to the event. Students redesign a setting and confront displacement."),
    ("SOC3333_PatternNotReason.html", "criminology", "Criminology", "The Pattern Is Not the Reason",
     "A writing lab for the moment a paper stalls, when a student has found a real pattern, reported it accurately, and stopped short of explaining it."),
    ("SOC3333_AskableQuestion.html", "criminology", "Criminology", "The Askable Question",
     "Narrowing a topic into a question that can actually be answered, and finding peer-reviewed sources that speak to it rather than sources that merely share its vocabulary."),
    ("SOC3333_ApplyTheTheory.html", "criminology", "Criminology", "Apply the Theory",
     "Naming a theory is not applying one. The lab walks students from restating what a theory says to putting its mechanism to work on their own case."),
    ("SOC3333_HomeStretch.html", "criminology", "Criminology", "The Home Stretch",
     "An end-of-semester synthesis lab that turns four short scaffolded papers into one coherent account of what criminology knows about a single offense type."),

    ("WCC_Lab01_WhoCounts.html", "wcc", "White-Collar Crime", "Who Counts",
     "Every count of white-collar crime starts with a definition, and the definitions disagree. Students sort real events under offender-based and offense-based definitions and see the totals move."),
    ("WCC_Lab02_FollowTheHarm.html", "wcc", "White-Collar Crime", "Follow the Harm",
     "There is no national count of white-collar crime. There are a handful of general counting systems plus separate enforcement records at every regulatory agency with a statute. Students try to assemble a total and find out why nobody has."),
    ("WCC_Lab03_FraudTriangle.html", "wcc", "White-Collar Crime", "The Fraud Triangle",
     "Cressey interviewed 133 people imprisoned for violating financial trust and asked what had to be true for each of them. Students test the resulting triangle against cases it was not built from."),
    ("WCC_Lab04_SanctionThreat.html", "wcc", "White-Collar Crime", "The Sanction Threat",
     "A replication of the Paternoster and Simpson scenario study, in which managers weigh formal sanctions, informal sanctions, and moral inhibition. Students answer first and compare against the published results."),
    ("WCC_Lab05_DenyingTheGuiltyMind.html", "wcc", "White-Collar Crime", "Denying the Guilty Mind",
     "Benson found that convicted white-collar offenders rarely denied the acts. They denied the criminality. Students classify real accounts and locate the line between explanation and excuse."),
    ("WCC_Lab06_DiffusionOfFraud.html", "wcc", "White-Collar Crime", "Diffusion of Fraud",
     "A real oil and gas investment fraud that began as a legitimate business, reconstructed from the record, so students can watch the point at which the enterprise crossed over."),
    ("WCC_Lab07_PonziMachine.html", "wcc", "White-Collar Crime", "The Ponzi Machine",
     "A runnable model of a scheme financed by the people who have not yet found out. Students set the promised return and inflow rate and watch the arithmetic of collapse."),
    ("WCC_Lab08_PriceOfADeath.html", "wcc", "White-Collar Crime", "The Price of a Death",
     "Workplace fatality investigations and the penalties that follow them. Students work with the enforcement record and compare the sanction against the harm."),
    ("WCC_Lab09_ECHO.html", "wcc", "White-Collar Crime", "ECHO",
     "A guided exercise in the Environmental Protection Agency's public compliance database, in which students look up real facilities, read what inspectors found, and see what was done about it."),
    ("WCC_Lab10_ThePaycheck.html", "wcc", "White-Collar Crime", "The Paycheck",
     "Wage theft as a property crime, worked through a pay stub. Students calculate what was taken, identify the mechanism, and compare it against the enforcement route available to the worker."),
    ("WCC_Lab11_SwapOrBet.html", "wcc", "White-Collar Crime", "Swap or Bet",
     "A contract that pays if a team wins is a swap under the Commodity Exchange Act and a bet under the Texas Penal Code. Students classify real products and defend the line they drew."),
    ("WCC_Lab12_TheDeal.html", "wcc", "White-Collar Crime", "The Deal",
     "Most corporate crime in the United States is resolved by agreement rather than by trial. Students read real deferred and non-prosecution agreements and weigh what each side obtained."),
]

COURSES = [("all", "All labs"), ("intro", "Introduction to Sociology"),
           ("criminology", "Criminology"), ("wcc", "White-Collar Crime")]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Teaching Resources | Nicholas J. Membrez-Weiler</title>
<meta name="description" content="A free repository of {n} browser-based sociology and criminology teaching labs covering introductory sociology, criminology, and white-collar crime. No accounts, no tracking, free to adapt.">
<link rel="canonical" href="https://membrezweiler.com/teaching-resources.html">
<meta property="og:title" content="Teaching Resources | Nicholas J. Membrez-Weiler">
<meta property="og:description" content="{n} free browser-based teaching labs for sociology and criminology courses.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://membrezweiler.com/teaching-resources.html">
<meta property="og:image" content="https://membrezweiler.com/assets/img/nicholas-membrez-weiler.jpg">
<meta name="twitter:card" content="summary">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
<script>(function(){{try{{var t=localStorage.getItem('mw-theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">Nicholas J. Membrez-Weiler<span>Sociology</span></a>
    <nav class="site-nav" aria-label="Primary">
      <a href="index.html">Home</a>
      <a href="research.html">Research</a>
      <a href="teaching.html">Teaching</a>
      <a href="teaching-resources.html" aria-current="page">Teaching Resources</a>
      <a href="students.html">Students</a>
      <a href="service.html">Service</a>
      <a href="cv.html">CV</a>
    </nav>
    <button class="theme-toggle" type="button" aria-label="Switch to dark theme">
      <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.2 5.2l1.4 1.4M17.4 17.4l1.4 1.4M18.8 5.2l-1.4 1.4M6.6 17.4l-1.4 1.4"/></svg>
      <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>
    </button>
  </div>
</header>

<main id="main">

  <div class="page-head">
    <div class="wrap">
      <p class="eyebrow">Teaching Resources</p>
      <h1>Sociology labs, free to use</h1>
      <p class="lede">{n} self-contained teaching labs for introductory sociology, criminology, and white-collar crime. Each one opens in a browser, holds real published data or real cases, and asks students for a judgment before it shows them the evidence.</p>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <div class="grid grid-2">
        <div class="prose">
          <h2>What these are</h2>
          <p>I write these for my own classes, and I run them during class rather than assigning them as homework. A lab takes somewhere between fifteen and forty minutes. The pattern is nearly always the same: a student is asked to commit to an estimate, a classification, or a judgment, and only then does the page show what the published data or the case record says. The gap between the two is the lesson.</p>
          <p>They are plain web pages. There is no account to create, no server behind them, and nothing a student enters is transmitted anywhere, which means they work on a phone, on a laptop, from a projector, or from a link posted in a learning management system. Students copy their finished work out of the page and submit it however the course normally collects work.</p>
          <p>You are welcome to use any of these in your own teaching, to change them, and to strip my course references out. If you build on one, I would be glad to hear about it.</p>
        </div>
        <aside class="panel">
          <h3>Using them in your course</h3>
          <dl class="definition-list">
            <dt>To assign one</dt>
            <dd>Link directly to the lab page, or download the file and host it yourself. Each lab is a single HTML file with everything inside it.</dd>
            <dt>To edit one</dt>
            <dd>Save the page, open it in any text editor, and change the text or the data. There is no build step and no framework.</dd>
            <dt>Student privacy</dt>
            <dd>Responses stay in the browser. Nothing is sent to me or to anyone else.</dd>
            <dt>Reuse</dt>
            <dd>Free for educational use with attribution. Please keep a credit line if you adapt one.</dd>
          </dl>
        </aside>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="rule-label">Browse the repository</p>

      <div class="lab-controls">
        <label class="visually-hidden" for="lab-search">Search labs</label>
        <input class="lab-search" id="lab-search" type="search" placeholder="Search by title, topic, or concept" autocomplete="off">
        <div class="filter-set" role="group" aria-label="Filter by course">
{filters}
        </div>
      </div>

      <p class="lab-count" id="lab-count">Showing all {n} labs.</p>

      <ul class="lab-grid" id="lab-grid">
{cards}
      </ul>

      <p class="no-results" id="lab-empty" hidden>No labs match that search. Try a different word, or clear the filters.</p>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="wrap">
    <div>
      <p><strong>Nicholas J. Membrez-Weiler</strong></p>
      <p>Department of Sociology, Midwestern State University</p>
      <p><a href="mailto:nicholas.membrez@msutexas.edu">nicholas.membrez@msutexas.edu</a></p>
    </div>
    <div>
      <p><strong>Elsewhere</strong></p>
      <p><a href="https://orcid.org/0009-0000-8866-0836">ORCID</a></p>
    </div>
    <nav class="footer-nav" aria-label="Footer">
      <a href="research.html">Research</a>
      <a href="teaching.html">Teaching</a>
      <a href="teaching-resources.html">Teaching Resources</a>
      <a href="students.html">Students</a>
      <a href="service.html">Service</a>
      <a href="cv.html">CV</a>
    </nav>
  </div>
</footer>

<script src="assets/js/site.js" defer></script>
</body>
</html>
"""

def main():
    site = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
    missing = [f for f, *_ in LABS if not os.path.exists(os.path.join(site, "labs", f))]
    if missing:
        raise SystemExit("Missing lab files: " + ", ".join(missing))

    filters = "\n".join(
        '          <button class="filter-btn" type="button" data-filter="{k}" aria-pressed="{p}">{l}</button>'.format(
            k=k, l=html.escape(l), p="true" if k == "all" else "false")
        for k, l in COURSES)

    anchors = {"intro": "intro", "criminology": "criminology", "wcc": "wcc"}
    seen = set()
    cards = []
    for fn, key, label, title, desc in LABS:
        anchor = ""
        if key not in seen:
            seen.add(key)
            anchor = ' id="{}"'.format(anchors[key])
        cards.append(
            '        <li class="lab" data-course="{k}"{a}>\n'
            '          <p class="lab-course">{c}</p>\n'
            '          <h3><a href="labs/{f}" target="_blank" rel="noopener">{t}</a></h3>\n'
            '          <p>{d}</p>\n'
            '          <p class="lab-open"><a href="labs/{f}" target="_blank" rel="noopener">Open the lab<span class="visually-hidden">: {t}</span></a></p>\n'
            '        </li>'.format(k=key, a=anchor, c=html.escape(label), f=fn,
                                   t=html.escape(title), d=html.escape(desc)))

    out = HEAD.format(n=len(LABS), filters=filters, cards="\n".join(cards))
    with open(os.path.join(site, "teaching-resources.html"), "w", encoding="utf-8") as fh:
        fh.write(out)
    print("wrote teaching-resources.html with", len(LABS), "labs")

if __name__ == "__main__":
    main()
