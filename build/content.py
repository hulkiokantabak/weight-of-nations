# -*- coding: utf-8 -*-
# AUTO-GENERATED from the Seventh-Edition manuscript by parse_manuscript.py.
# Edit the manuscript + re-run the parser; do not hand-edit.
SECTIONS = [{'k': 'masthead',
  'kicker': 'A data essay · economic history · seventh edition',
  'h1': 'The Shifting Weight of Nations',
  'standfirst': '<i>Five centuries of world GDP, the two rulers that make the same country look mighty or modest, '
                'and the one variable underneath them both.</i>',
  'byline': 'Directed &amp; written by Hulki Okan Tabak',
  'dateline': [('Inspired by',
                "Stephen Kotkin on Hoover's <i>Uncommon Knowledge</i> (host Peter Robinson) — "
                'youtube.com/watch?v=gBEdxb8ei_0'),
               ('Span', '1500–2026, with a 2050 demographic horizon'),
               ('Lenses', 'deep history · manufacturing · technology · geopolitics · the future'),
               ('Edition', 'Seventh (fused &amp; panel-reviewed) · June 2026')]},
 {'k': 'argument',
  'hyp': "A nation's share of world GDP is not one number but three multiplied together — its share of the world's "
         'people, its price level (the ruler you measure with), and its productivity (output per person relative to '
         'the world). Strip away the first two and the entire five-century drama of rise, fall, and "re-convergence" '
         'collapses onto a single variable, productivity — which is also the only one that will decide the next '
         'fifty years.',
  'approach': 'Separate the two rulers (market-rate nominal and price-adjusted PPP); add the population-adjusted '
              'multiplier that turns a share into a statement about prosperity; triangulate three datasets kept '
              "deliberately un-stitched — Maddison for deep history, World Bank WDI for the modern era, the IMF's "
              'April 2026 vintage as a present-day marker; weigh every share against the world totals it is a '
              'fraction of; decompose the picture by bloc and by who-gained-and-lost; read every economy through all '
              'three lenses, country by country; and read every number for direction and order of magnitude, '
              'ruler-labelled, never for its decimals.',
  'concl': 'Seven conclusions follow, set out at the end. The shortest version: size is headcount; weight is '
           'productivity; and the future belongs to whoever holds the frontier of energy and knowledge — not to '
           'whoever holds the most people.'},
 {'k': 'section', 'num': 'Totals', 'title': 'The World This Essay Divides'},
 {'k': 'lede',
  't': '<i>Every share in these pages is a slice of three totals. Here they are first, before any country claims a '
       'fraction of them.</i>'},
 {'k': 'table',
  'headers': ['The whole', 'Total (2026, IMF WEO April 2026)', 'The ruler it speaks'],
  'rows': [['<b>People</b>',
            '~8.2 billion (8.16bn in 2024 → ~9.66bn by 2050)',
            'headcount — the denominator of the multiplier'],
           ['<b>World GDP at market exchange rates</b>',
            '<b>$126.3 trillion</b> (current US dollars)',
            'nominal — financial command, imports, debt, reserves'],
           ['<b>World GDP at purchasing power parity</b>',
            '<b>$222.8 trillion</b> (current international dollars)',
            'PPP — real output valued at common prices']]},
 {'k': 'p',
  't': 'The two GDP totals are the same world economy seen through the two rulers this essay keeps apart: $126.3 '
       'trillion is what global output is worth at market exchange rates; $222.8 trillion is what it amounts to once '
       'local price levels are equalised. The roughly <b>$96 trillion</b> between them is the price-level term from '
       'the hypothesis, written at planetary scale — the world\'s "PPP uplift." Population is the third number and '
       'the one that converts any share into a statement about how people actually live. Section 1A returns to these '
       'totals in full, with the lane distinctions and the denominator warnings; everything in between is the story '
       'of how the slices move.'},
 {'k': 'section', 'num': 'Reading', 'title': 'How to Read This Essay'},
 {'k': 'p',
  't': 'Most confusion in this subject comes from one mistake: letting a single GDP number do three different jobs. '
       'A share of world GDP can describe real output, financial command, or per-person productivity, depending on '
       'the ruler in use — and most arguments about "who is biggest" are really arguments about which ruler the '
       'speaker reached for, usually without saying so. Before any chart, match the question to the instrument.'},
 {'k': 'table',
  'headers': ["The question you're asking", 'Reach for', 'Because', 'The trap if you stop there'],
  'rows': [['Who is biggest in <b>real output</b>?',
            '<b>PPP</b> GDP share',
            'It values a haircut in Delhi and one in Zurich at a common price, so it measures volume, not price.',
            'It overstates command over things bought at world prices — chips, jet engines, dollar debt.'],
           ['Who commands <b>dollars, imports, assets, external finance</b>?',
            '<b>Nominal</b> share',
            'It tracks what output is worth on world markets — imports, collateral, reserves, what you can borrow '
            'against.',
            'It lurches with the currency cycle and asset prices, not only with real growth.'],
           ['Who is actually <b>rich</b> — output per person?',
            'The <b>multiplier</b> (PPP per head)',
            'GDP share divided by population share separates size from prosperity.',
            'It is blind to inequality, quality, public goods, and the informal economy.'],
           ['Why did Japan look so <b>huge in the 1990s</b>?',
            'The <b>FX chapter</b>',
            'The super-yen and asset bubble capitalised Japanese output at a world-market price PPP never endorsed.',
            'Mistaking a currency cycle for economic destiny.'],
           ['Five centuries of <b>comparison</b>?',
            '<b>Maddison-style PPP</b> benchmarks',
            'Market exchange rates simply do not exist for 1500 or 1700.',
            'The numbers are reconstructions with wide error bars — read shape, not decimals.'],
           ['<b>Coalition or bloc</b> weight?',
            '<b>Both</b> rulers, summed across members',
            'Alliances need real capacity and financial command at once.',
            '"The bloc" is not a fixed object — the EU, Europe, and the UK are different sets.']]},
 {'k': 'p',
  't': 'The operating rule that runs through every page: <b>read the ruler first, the direction second, and the '
       'decimal point last.</b> The direction is usually robust. The decimals, especially before 1900, are estimates '
       'wearing the costume of precision.'},
 {'k': 'section', 'num': 'Section 1', 'title': 'The Executive Answer'},
 {'k': 'lede', 't': '<i>The story is right. The ruler keeps changing.</i>'},
 {'k': 'p',
  't': 'A Kotkin-style narrative compresses the world into a few memorable numbers: the United States around a '
       'quarter of world GDP with about a twentieth of humanity; Japan from almost eighteen percent to under four; '
       'Europe sliding; China returning; India mostly absent. The narrative is useful. It is also dangerous unless '
       'every number is labelled with its measuring stick.'},
 {'k': 'p',
  't': 'The clean revision is this. Market exchange rates measure financial and market weight; PPP measures real '
       'output at common prices; the multiplier measures output per person relative to the world average. A country '
       'can be enormous because it has many people. It can be rich because each person produces a lot. It can be '
       'financially commanding because global markets price its output, currency, securities, institutions, and '
       'legal order at a premium. These are related, but they are not the same thing.'},
 {'k': 'p',
  't': 'The conclusion is not that America is safe forever, that China is destined to dominate, or that Europe is '
       'doomed. It is that aggregate share, per-person prosperity, market command, and geopolitical capacity are '
       'different layers of power. A serious account must keep them apart long enough to see how they interact.'},
 {'k': 'table',
  'headers': ['Entity', 'Nominal %', 'PPP %', 'Population %', 'Nominal ×', 'PPP ×'],
  'rows': [['United States', '26.34', '15.07', '4.23', '6.23', '3.56'],
           ['EU-27', '17.88', '14.36', '5.59', '3.20', '2.57'],
           ['EU-27 + UK', '21.25', '16.49', '6.45', '3.29', '2.56'],
           ['United Kingdom', '3.38', '2.14', '0.86', '3.93', '2.48'],
           ['China', '17.17', '19.72', '17.51', '0.98', '1.13'],
           ['India', '3.58', '8.36', '18.03', '0.20', '0.46'],
           ['Japan', '3.69', '3.35', '1.54', '2.40', '2.18'],
           ['Russia', '1.96', '3.57', '1.78', '1.10', '2.00']]},
 {'k': 'p',
  't': '<i>World Bank WDI country-sum, 2024. Nominal × is market-weight per person; PPP × is real-output per person '
       'relative to the world average. China is huge on PPP but only just above the world average per person. India '
       'is huge in people and potential but still below half the world average per person. The US is smaller than '
       'China on PPP aggregate output but much richer and more financially weighty per person.</i>'},
 {'k': 'section', 'num': 'Section 1A', 'title': 'The Totals Behind the Shares'},
 {'k': 'lede', 't': '<i>Percentages need denominators; the denominators are world GDP and world population.</i>'},
 {'k': 'p',
  't': 'A share of world GDP is a fraction. The numerator is a country or bloc; the denominator is the world. Leave '
       'the denominator invisible and the reader hears only drama — twenty-five percent, eighteen, four, seventeen. '
       'But the denominator itself has changed radically, and it is measured by the same two rulers as everything '
       'else.'},
 {'k': 'p',
  't': '<b>The market-priced world.</b> In the IMF WEO April 2026 marker, world nominal GDP is about <b>$126.3 '
       'trillion</b> in current US dollars. That is the market-exchange-rate world: dollars, imports, external '
       'finance, reserve assets, sanctions exposure, and global pricing.'},
 {'k': 'p',
  't': '<b>The common-priced world.</b> In the same vintage, world GDP at PPP is about <b>$222.8 trillion</b> in '
       'current international dollars. That is the common-price world — real domestic output adjusted for local '
       'price levels. It is larger because many goods and services in lower-income economies cost less than their '
       'market exchange rates imply.'},
 {'k': 'p',
  't': "<b>The headcount.</b> The UN's World Population Prospects 2024 puts world population at about <b>8.16 "
       'billion</b> in 2024, roughly <b>9.66 billion</b> by 2050, and about 10.18 billion by 2100, peaking near 10.3 '
       'billion in the mid-2080s before the first sustained fall of the modern era. That matters because the '
       'multiplier is GDP share divided by population share: a country can gain share by adding people, by raising '
       'output per person, or by being priced more highly by the ruler in use.'},
 {'k': 'table',
  'headers': ['Measure', 'Current total', 'Source lane', 'Interpretation'],
  'rows': [['World nominal GDP',
            '$126.3 trillion',
            'IMF WEO April 2026, 2026 projection, current US dollars',
            'Market-exchange-rate denominator for financial command, imports, dollar debt, valuation, sanctions.'],
           ['World GDP at PPP',
            '$222.8 trillion',
            'IMF WEO April 2026, 2026 projection, current international dollars',
            'Real-output denominator at common prices. Not spendable FX; a statistical purchasing-power dollar.'],
           ['World population',
            '8.16bn (2024) → ~9.66bn (2050) → peak ~10.3bn (2080s)',
            'UN WPP 2024, medium variant',
            'The denominator for the multiplier. Growth slows, but the world still adds ~1.5bn people by 2050.'],
           ['Report internal lane',
            '~$110T nominal; ~$170T PPP (constant 2021 int\\$, ≈$195T current); 8.05bn — 2024',
            'WDI/QoG country-sum',
            'Used for the internal share and multiplier arithmetic, against a single common denominator.']]},
 {'k': 'p',
  't': '<b>Denominator warning.</b> This report carries two modern denominators and keeps them apart by design. '
       'Official IMF/World Bank world aggregates are best for a current global total; the WDI/QoG country-sum '
       'denominator is best for the internal share arithmetic, because every entity is then measured against the '
       'same source lane. The two are close enough for the argument but not identical — a few tenths of a percentage '
       'point apart. A third lane, the WDI <b>constant 2021 international-dollar</b> series (~$170T for 2024), '
       'values real output at a fixed benchmark and is lower again. These three PPP totals — $222.8T (2026 current), '
       '~$195T (2024 current), ~$170T (2024 constant-2021) — answer different questions and are never spliced into '
       'one line.'},
 {'k': 'section', 'num': 'Section 2', 'title': 'One Identity, Three Lenses'},
 {'k': 'lede', 't': '<i>Before the curves, the algebra — because it is the whole argument in one line.</i>'},
 {'k': 'p', 't': "Any country's share of world output can be written as the product of three ratios:"},
 {'k': 'identity'},
 {'k': 'p',
  't': 'Read left to right, this is why the charts that follow disagree with one another. <b>Population</b> explains '
       'why China and India were "huge" in 1700 and why they are rising again now. The <b>price level</b> is the '
       'ruler — the entire gap between the nominal and PPP pictures — and it moves with currencies and inflation as '
       'much as with real output. <b>Productivity</b> is what is left when you divide the first two out: output per '
       'person, relative to the world average. That last term is what this essay is really about. It is what the '
       'Great Divergence created, what the Asian re-convergence has so far barely touched, and what the technologies '
       'of the next half-century will redistribute.'},
 {'k': 'p', 't': 'This report therefore refuses a single master line. It uses three lenses and keeps them labelled.'},
 {'k': 'table',
  'headers': ['Lens', 'Question it answers', 'Best use', 'Misuse'],
  'rows': [['<b>Nominal GDP share</b>',
            'What is the economy worth at market exchange rates?',
            'Imports, debt, reserves, traded goods, financial command, sanctions, valuation.',
            'Treating currency swings as pure real growth or decline.'],
           ['<b>PPP GDP share</b>',
            'How much real output is produced at common prices?',
            'Cross-country real output, living standards, centuries-long history.',
            'Pretending PPP buys imported chips, jet engines, oil, or dollar debt at local prices.'],
           ['<b>Multiplier</b>',
            'Output per person relative to the world average?',
            'Separating size from prosperity, population from productivity.',
            'Ignoring inequality, quality, public goods, and strategic conversion.']]},
 {'k': 'section', 'num': 'Section 3', 'title': 'PPP Explained Slowly'},
 {'k': 'lede', 't': '<i>PPP is necessary. PPP is insufficient. Both statements matter.</i>'},
 {'k': 'p',
  't': 'Purchasing power parity begins with a simple observation: prices differ across places. A dollar converted at '
       'the market rate buys a different bundle in Delhi, Tokyo, Istanbul, Zurich, or Kansas. Non-traded services '
       'are especially different — a haircut, rent, local transport, a bowl of rice can cost far less in a '
       'lower-income country. Compare GDP only at market exchange rates and you may badly understate the real volume '
       'of domestic goods and services in lower-price economies. PPP corrects that by asking what GDP would look '
       'like priced with a common international structure rather than market rates. That is why China and India '
       'become much larger on PPP charts than on nominal ones — and why PPP is the right ruler for real output, '
       'material well-being, and long-run history.'},
 {'k': 'p',
  't': '<b>What PPP gets right.</b> It values output at common prices, so low-price economies are not mechanically '
       'shrunk by weak currencies. It is closer to domestic command over local goods and services than nominal '
       'dollars are. It is the only plausible ruler before modern exchange-rate markets existed. And it lets us see '
       'when a populous country is actually producing large real output rather than merely receiving a low dollar '
       'price.'},
 {'k': 'p',
  't': '<b>Where PPP wobbles — and it does.</b> It is not a currency you can spend abroad, not a reserve asset, and '
       'it does not mean that Chinese, Indian, Russian, or Turkish income can buy semiconductors, aircraft engines, '
       'oil, LNG cargoes, medical devices, dollar bonds, or naval hardware at local service-sector prices. The PPP '
       'dollar is a statistical dollar, not a shipping invoice. It also depends on price surveys, national accounts, '
       'expenditure weights, imputation, and benchmark years. The International Comparison Program behind it runs '
       'only every six years or so, covers thousands of goods across some 180 countries, and is genuinely hard: the '
       "2005 round cut China's and India's estimated real incomes by roughly 40 percent overnight; the 2011 round "
       "then raised China's by about 20 percent. Current PPP figures carry something like <b>±5–10 percent "
       'structural uncertainty</b> — materially more than directly reported nominal figures — and the famous 2014 '
       '"China overtakes the US" story was, strictly, premature.'},
 {'k': 'table',
  'headers': ['PPP shortcoming', 'How to interpret it'],
  'rows': [['Imports and traded goods',
            'PPP overstates command over goods bought at world prices. Use nominal or external-balance measures.'],
           ['Debt and reserves', 'Dollar debt and reserves are nominal claims. PPP does not pay them.'],
           ['Military procurement',
            'Domestic labour may be PPP-relevant; imported chips, engines, sensors, and machine tools are '
            'nominal/traded.'],
           ['Quality and inequality',
            'PPP averages do not guarantee equivalent quality, distribution, public goods, or household welfare.'],
           ['Revisions',
            'ICP rounds move countries by tens of percent; historical reconstructions have wide error bands.'],
           ['Exchange-rate forecasting',
            'PPP says nothing about where a currency should trade tomorrow; never use it as a standalone valuation '
            'signal.']]},
 {'k': 'p',
  't': 'PPP in one sentence: it is the best ruler for real output at common prices, nominal is the better ruler for '
       'world-market command, and the multiplier turns either into a per-person punch. None of the three should be '
       'used alone.'},
 {'k': 'section', 'num': 'Section 4', 'title': 'Deep History — The Contested Origins'},
 {'k': 'lede', 't': '<i>The long arc is a population story until it becomes a technology story.</i>'},
 {'k': 'fig',
  'key': 'long_bar',
  'num': 'Fig. 01',
  'title': 'Five centuries of relative economic size',
  'sub': '',
  'caption': 'PPP-style world GDP shares at benchmark years, 1500–2024, shown as benchmark bars (honest about where '
             'data exists) so the agrarian-Asia → Western-surge → Asian-re-convergence rotation is visible without '
             'inventing decades nobody measured.'},
 {'k': 'fig',
  'key': 'long_area',
  'num': 'Fig. 02',
  'title': 'The same five centuries as a re-sliced pie',
  'sub': '',
  'caption': "The cumulative 100% view; seductive precisely because it looks continuous, which is why Figure 01's "
             'honest gaps sit beside it.'},
 {'k': 'p',
  't': 'Before industrialisation, aggregate economic size was heavily tied to population, land, calories, and '
       'labour. China and India were huge because they held large shares of humanity organised around intensive '
       'agriculture, urban craft, and long commercial traditions. That size should not be confused with rich-country '
       'living standards. A large preindustrial share often meant many people producing near-subsistence output, not '
       "a high multiplier. China's third of the world in 1820 was not a story of rich Chinese; it was a story of "
       'many Chinese, at roughly subsistence income, in a world where almost everyone lived at subsistence. '
       'Aggregate size in the pre-industrial era was very nearly a headcount.'},
 {'k': 'p',
  't': 'These deep-history numbers are estimates with wide error bars, and the scholarship is alive and quarrelsome. '
       "Angus Maddison's figures are the backbone of nearly every chart you will ever see, including these. But a "
       'school led by Stephen Broadberry, rebuilding national accounts from wages, prices, and tax records, has '
       'steadily revised the picture — and the revisions cut against the romance of a rich East suddenly overtaken. '
       'On their reconstructions the divergence in living standards between northwest Europe and the leading Asian '
       'economies began far earlier than the canonical "Great Divergence around 1800" of Kenneth Pomeranz and the '
       'California school: comparing the largest Asian state with the leading European ones, the gap is already '
       "visible by around 1400. China's Ming-era output per head has been marked down by up to a third; India looks "
       'prosperous at the Mughal peak around 1600, then drains away through the eighteenth century, before the '
       'British Raj proper even begins. So treat the headline "China ≈ 40%" as a rounded high-end ceiling — '
       "Maddison's own peak for China is closer to a third (~33% in 1820) — and even the textbook moment when the "
       'United States overtook Britain in output per head has been pushed back to the 1870s.'},
 {'k': 'p',
  't': 'If the divergence is real, what caused it? Three explanations compete, and the honest answer is that the '
       'field has not settled — so neither will this essay. The first is <b>ecological</b>: Pomeranz argues Britain '
       'happened to sit on accessible coal and to command New-World land that relieved the Malthusian ceiling, so '
       'its escape was as much luck and geography as genius. The second is <b>institutional</b>: in the tradition of '
       'Douglass North and, more recently, Acemoglu and Robinson, secure property, open inquiry, patentable return, '
       'and constraints on the sovereign let Europe convert invention into compounding growth. The third is the one '
       'the numbers keep gesturing at, and that a cyclical historian like Ibn Khaldun would press: institutional '
       'stagnation inside the great Asian empires, an agrarian-bureaucratic equilibrium that taxed the surplus '
       "without reinvesting it, so that Song China's medieval efflorescence never compounded into take-off. Joseph "
       "Needham's famous puzzle — why the civilisation that invented paper, printing, gunpowder, and the compass did "
       'not have the Scientific Revolution — lives in this third box.'},
 {'k': 'p',
  't': 'And there is a fourth factor the curves are unusually good at hiding, because a falling line names no '
       "culprit: <b>power</b>. India's share did not simply fail to rise; large parts of it were actively "
       'de-industrialised under a specific colonial relationship — a hollowing-out of its textile economy by a mix '
       'of British factory competition, the collapse of Mughal demand, and the policy architecture of conquest. The '
       'next chart makes that violence visible, because it measures the one thing GDP share blurs: who actually made '
       "the world's goods."},
 {'k': 'section', 'num': 'Section 5', 'title': 'Manufacturing, Not GDP'},
 {'k': 'lede',
  't': '<i>GDP share and industrial command are related, but not identical — and the manufacturing ruler moves far '
       'more violently.</i>'},
 {'k': 'fig',
  'key': 'mfg',
  'num': 'Fig. 03',
  'title': 'Share of world manufacturing output (Bairoch), 1750–1900',
  'sub': '',
  'caption': 'The most violent reversal in the whole story, and where the "China was a third of the world" figure '
             'actually comes from.'},
 {'k': 'p',
  't': 'Modern power did not come from GDP volume alone. It came from a particular kind of output: mechanised, '
       'scalable, energy-intensive production linked to finance, logistics, weaponry, and science. A country could '
       'stay large in agrarian output while losing strategic centrality if manufacturing shifted elsewhere.'},
 {'k': 'p',
  't': "In 1750, China (32.8%) and India (24.5%) together made about 57 percent of the world's manufactures — this, "
       'not GDP, is the source of the "Asia was a third of the world" figure people half-remember. Over the next 150 '
       'years it collapses: India to 1.7% by 1900, China to 6.2%. Meanwhile Europe as a whole climbs from 23% to 62% '
       '— the UK alone going from under 2% to nearly 23% at its 1880 peak — and the United States rockets from a '
       'rounding error to 24%. The non-Western share fell from 73% to 11%. The subtle part: even in 1750, when '
       "Britain made under 2% of world manufactures, its output per person already ran ahead of India's and China's. "
       "The non-Western collapse was not merely relative — India's and China's manufacturing output per head "
       "actually fell in absolute terms while Europe's multiplied roughly eightfold."},
 {'k': 'p',
  't': 'Two lessons travel out of this chart. First, "share of manufacturing" and "share of GDP" are different '
       'rulers again, and the manufacturing one moves far more violently — which is exactly why the round "a third / '
       '40 percent" number for old Asia feels so large: it is frequently the manufacturing figure smuggled into a '
       'GDP sentence. Second, and pointing forward to the thesis: what the West acquired in the nineteenth century '
       'was not a bigger population but a new way of converting energy into goods — coal and steam doing the work of '
       'millions of hands. That is the first appearance of the variable everything else reduces to.'},
 {'k': 'section', 'num': 'Section 6', 'title': "The Market-Weight Era — Kotkin's Actual Canvas"},
 {'k': 'lede',
  't': '<i>The same years, two different rulers; and most of his modern figures live on the nominal one.</i>'},
 {'k': 'fig',
  'key': 'nom',
  'num': 'Fig. 04',
  'title': 'World GDP share, nominal (market exchange rates), 1960–2024, current US dollars',
  'sub': '',
  'caption': 'Where "Japan 18%," "US 25%," and "Europe 30→17" live. Watch how much the lines move with currencies, '
             'not just with growth.',
  'controls': True},
 {'k': 'p',
  't': 'The modern period is where the soundbites live and where ruler confusion does the most damage. On market '
       'exchange rates the US runs from a postwar ~40% (1960) down toward a long-run ~25% — jaggedly, because '
       "exchange rates whip the figure around. Japan's 1995 spike to ~18% is the super-yen and the asset bubble, not "
       'real output doubling; the "lost decades" and a strong dollar then more than halve it. Europe\'s path wobbles '
       'with the euro. China is the one secular climb — under 2% in 1990, a peak near 18% in 2021, easing since. '
       'India barely moves on this ruler until very recently. Toggle the West bloc and the headline appears: the '
       'US-plus-allies share fell from about three-quarters to roughly half.'},
 {'k': 'fig',
  'key': 'us',
  'num': 'Fig. 05',
  'title': 'The American century in one line: US nominal share, 1913–2024',
  'sub': '',
  'caption': 'The ~50% "rubble peak" of 1945, bracketed by ~19% in 1913 and ~26% today.'},
 {'k': 'p',
  't': 'It pays to be precise about <i>why</i> a nominal line lurches, because "currency" is a lazy shorthand. A '
       "country's nominal share can move for four quite different reasons, and only the first is what most people "
       'think they are reading. <b>One:</b> real growth — it actually makes more stuff. <b>Two:</b> relative '
       "inflation — if its prices rise faster than the world's, its nominal GDP swells even with flat real output. "
       "<b>Three:</b> the exchange-rate cycle — when the dollar strengthens, every other country's "
       'dollar-denominated GDP shrinks mechanically, and the US share rises without a single extra widget. '
       '<b>Four:</b> policy — a managed currency, like the yuan, can be held down to protect exporters, suppressing '
       "the country's own measured nominal share. Japan's mountain and China's recent dip are both mostly reasons "
       'two and three, not one. Hold that four-way split; the dollar section makes it load-bearing.'},
 {'k': 'section', 'num': 'Section 7', 'title': 'The Multiplier — Strip Out Population'},
 {'k': 'lede', 't': '<i>This is the population-adjusted punch, and it is the chart that breaks the myth.</i>'},
 {'k': 'fig',
  'key': 'mult',
  'num': 'Fig. 06',
  'title': 'Income relative to the world average, PPP, 1820–2024',
  'sub': '',
  'caption': 'GDP share ÷ population share; the dashed line is the world mean (1.0).'},
 {'k': 'p',
  't': 'The multiplier is the most intuitive and most neglected measure in the conversation. It is simply GDP share '
       'divided by population share. A country with 25 percent of world GDP and 5 percent of world population '
       "produces about five times the world-average output per person. A multiplier of 1.0 is the world's per-capita "
       'mean; 3.0 means three times as rich as the typical human.'},
 {'k': 'p',
  't': "The multiplier turns size into prosperity, and it turns the rise of Asia into a more precise story. China's "
       '"mighty" 33% of 1820 was a multiplier of just 0.9 — its people sat at, even slightly below, the world '
       'average. It then crashed to 0.2 across the century of humiliation and the Mao era, and has only just clawed '
       'back to about 1.1. India is at ~0.46: real progress, still under half the world average, a stage behind '
       'China. Meanwhile the US (≈3.6×) and Western Europe (≈2.7×) have sat three to four times above the mean for '
       "over a century, and Japan's leap from ~0.9 to ~3 is the postwar miracle in a single line."},
 {'k': 'pull',
  't': '<b>The rise of Asia in size is largely population weight returning. The rise of Asia in prosperity has '
       'barely begun.</b>'},
 {'k': 'p',
  't': "It is worth pausing on what a multiplier of 0.46 means, because the decimal hides a person. India's figure "
       'is a distance: between a life in Munich and a life in Bihar, between a clinic with an MRI and a clinic with '
       "a queue, multiplied across one and a half billion people. China's climb from 0.2 to 1.1 is the largest "
       "movement of human beings out of poverty in recorded history — and it still only reaches the world's middle. "
       'Every share point in every chart here contains hundreds of millions of such lives; the multiplier is the '
       'closest any of these numbers comes to telling you how those lives are lived. That is the difference between '
       'counting people and weighing what their days contain.'},
 {'k': 'section', 'num': 'Section 8', 'title': 'The Same Year, Measured Four Ways'},
 {'k': 'lede', 't': '<i>Drop the five-century arc and hold a single year still.</i>'},
 {'k': 'fig',
  'key': 'share24',
  'num': 'Fig. 07',
  'title': 'Nominal vs PPP share of world GDP, 2024',
  'sub': '',
  'caption': 'Darker bar = market exchange rates, lighter = PPP.'},
 {'k': 'p',
  't': 'Switching from market rates to PPP lowers the share of high-price economies — the US (26→15), the EU '
       '(18→14), Japan, the UK — and raises the share of lower-price, populous ones — China (17→20, overtaking the '
       'US), India (3.6→8.4), Russia. This is why Kotkin\'s "Europe ≈ 17%" matches the PPP figure for Europe while '
       'his "Japan 18%" and "US 25%" use the nominal one. Both columns are correct; they answer different questions '
       '— financial weight on the dark bars, real output on the light.'},
 {'k': 'fig',
  'key': 'gap24',
  'num': 'Fig. 08',
  'title': 'The 2024 ruler gap',
  'sub': '',
  'caption': 'Nominal share minus PPP share, percentage points; positive = nominal-heavy, negative = PPP-lifted.'},
 {'k': 'p',
  't': 'Stack those two columns into a single bar per country and the gap becomes a number in its own right — the '
       'cleanest one-glance map of who the dollar flatters and whom PPP lifts. Positive bars are economies that look '
       'bigger in dollars than in real volume: the United States most of all (+11.3 points), where high domestic '
       'prices and the reserve-currency premium inflate the dollar value of output; then Europe and the UK. Negative '
       'bars are economies PPP lifts: India (−4.8), China (−2.5), and Russia. The size of each bar is, in effect, '
       'the price-level term from the opening identity, read off one economy at a time. It is also a preview of the '
       "convergence clock: a converging country's positive gap grows as its prices rise toward the frontier's."},
 {'k': 'fig',
  'key': 'mult24',
  'num': 'Fig. 09',
  'title': 'Income vs world average, 2024 — nominal vs PPP',
  'sub': '',
  'caption': 'The fulcrum is China.'},
 {'k': 'p',
  't': "If the ruler changed only the totals, every pair would scale together. It doesn't — and one country flips "
       'sides. On the nominal ruler the US looks like a 6.2× colossus; on PPP it is a still-formidable but humbler '
       '3.6×. The UK and Russia move most in proportion. But the verdict for almost every economy survives the '
       'switch — except China, at 0.98× nominal and 1.13× PPP. On one ruler the average Chinese citizen is just '
       'below the world mean; on the other, just above. The single most consequential country on earth straddles the '
       'parity line, and which side it lands on is a measurement choice. India, at 0.20× nominal and 0.46× PPP, is '
       'unambiguously below on either.'},
 {'k': 'fig',
  'key': 'scatter24',
  'num': 'Fig. 10',
  'title': 'Population weight vs real-output weight, 2024',
  'sub': '',
  'caption': 'The multiplier, drawn as a map: the diagonal is parity, and the vertical distance from it is the '
             'multiplier.'},
 {'k': 'p',
  't': 'The United States, Europe, Japan and the UK float high above the line on small populations — the frontier '
       'economies. China sits almost exactly on it, the giant that has reached the middle. India sits far below and '
       'to the right: more than a sixth of humanity, still well under the parity line. The whole essay is an '
       'argument about how points move toward that line, or away.'},
 {'k': 'section', 'num': 'Section 9', 'title': 'The FX Chapter — Japan and the Price-Level Clock'},
 {'k': 'lede', 't': '<i>Currency cycles can masquerade as economic destiny.</i>'},
 {'k': 'fig',
  'key': 'jp',
  'num': 'Fig. 11',
  'title': 'Japan, the warning label: one country, two rulers, 1990–2024',
  'sub': '',
  'caption': 'Solid = nominal, dashed = PPP.'},
 {'k': 'p',
  't': 'The Japan claim is the cleanest warning label in the whole debate. Its nominal share peaks at about 18 '
       'percent in 1994 — the super-yen and the asset bubble capitalising Japanese output at a world-market price — '
       'then more than halves as the bubble deflates and the dollar strengthens. The PPP line never crosses ~8 '
       'percent and slides quietly to ~3.4 percent today. The gap between the two is the currency-and-price-level '
       'premium, not a doubling of real output. Japan is the cleanest proof in the essay that a number can halve on '
       'one ruler while the thing it claims to measure — real output per person — barely moves.'},
 {'k': 'p',
  't': 'The right revision is to refuse the habit of treating nominal GDP as a sloppy measure. Nominal GDP is the '
       'correct measure for certain questions: imports, external debt, reserves, dollar finance, market '
       'acquisitions, sanctions, and the price paid for traded goods. It is just the wrong measure for others: '
       'domestic real output and average material well-being.'},
 {'k': 'table',
  'headers': ['Nominal share moves with', 'What it means'],
  'rows': [['Real growth', 'More output can raise nominal share.'],
           ['Relative inflation', 'Higher domestic prices can lift dollar GDP without equivalent volume gain.'],
           ['Exchange rates', 'A strong currency can inflate share; depreciation can hide real volume.'],
           ['Asset / capital-market valuation',
            'Bubbles and risk premia can enter the national market-weight story.'],
           ['Capital controls / sanctions', 'A country can have PPP volume but weak external convertibility.']]},
 {'k': 'section', 'num': 'Section 10', 'title': "Geopolitics (I) — Who Really Paid for China's Rise"},
 {'k': 'lede',
  't': '<i>Start with the peak everyone cites — the most misleading true sentence in the whole debate.</i>'},
 {'k': 'p',
  't': 'In 1945 the United States held something like 50 percent of global output in nominal terms, plus 80 percent '
       "of the world's hard-currency reserves and over half its manufacturing. But that share measured the rest of "
       'the world lying in rubble as much as American strength: Germany, Japan, Britain, France and the USSR had had '
       'their industrial bases bombed, blockaded, or bled. As they rebuilt, the US share had to fall even as '
       'American output kept growing. By 1960 it was about 40 percent nominal; on the price-adjusted PPP ruler, the '
       'US "high noon" around 1950 was already only ~27 percent. Same country, same era — 50, 40, or 27 percent '
       'depending entirely on the year and the ruler. Any single headline number here is a choice, not a fact.'},
 {'k': 'fig',
  'key': 'bloc',
  'num': 'Fig. 12',
  'title': 'US-plus-allies vs China-plus-India, both rulers, 1990–2024',
  'sub': '',
  'caption': 'WDI country-sum; solid = nominal, dashed = PPP.'},
 {'k': 'fig',
  'key': 'delta',
  'num': 'Fig. 13',
  'title': 'Who gained and lost world-GDP share, 1990–2024',
  'sub': '',
  'caption': 'Change in percentage points; darker = nominal, lighter = PPP.'},
 {'k': 'p',
  't': 'On the nominal ruler the industrial-allied bloc — US + EU + UK + Japan — falls from about 76% to 51% of '
       'world GDP since 1990, while China + India climb from ~3% to ~21%. On PPP the bloc falls further (59% → 35%) '
       'and China+India rise higher (7% → 28%), because PPP reweights lower-price economies up. Either way the bloc '
       'lost roughly a quarter of the world. But the decomposition overturns the lazy version of "Western decline." '
       'China gained ~16 points on both rulers. The losers are Europe (EU+UK, −13 points on both) and Japan (−11 '
       'nominal). <b>The United States is nearly flat in nominal terms (−1.1) — it held its quarter of the world for '
       "four decades — and only lower on PPP (−6.5) because everyone's PPP slice was diluted by the populous "
       'risers.</b> The headline "the West is in relative decline" is accurate; the sub-headline "and the United '
       'States is the part that declined" is not. America held its ground; its allies ceded theirs.'},
 {'k': 'p',
  't': 'That asymmetry — patron stable, clients shrinking — is the geopolitically loaded fact under all the '
       'arithmetic, and it cuts two ways. A patron whose allies shrink gains in relative standing but loses the very '
       'coalition that converts standing into power: alliances are a force-multiplier a bare GDP share does not '
       'show. The same numbers that comfort Washington should also unsettle it.'},
 {'k': 'p',
  't': 'GDP share is not geopolitical power by itself; it is a capacity measure that must be converted. Conversion '
       'requires fiscal extraction, institutions, military procurement, logistics, alliances, energy, technology, '
       'standards, and political legitimacy. A large economy with weak conversion can underperform strategically; a '
       'smaller economy inside a strong alliance and dollar system can overperform.'},
 {'k': 'table',
  'headers': ['GDP layer', 'What it can support', 'What can block translation into power'],
  'rows': [['PPP domestic volume',
            'Local labour, services, construction, domestic military inputs.',
            'Quality gaps, bottlenecks, corruption, weak logistics, import dependence.'],
           ['Nominal dollar output',
            'Imports, foreign debt service, reserves, market acquisitions.',
            'Currency depreciation, sanctions, capital controls, dollar funding stress.'],
           ['High multiplier',
            'Tax capacity, research systems, complex services, advanced firms.',
            'Inequality, political fragmentation, aging, fiscal rigidity.'],
           ['Large population',
            'Scale, labour force, domestic market, military manpower.',
            'Low human capital, weak job creation, energy scarcity, poor institutions.'],
           ['Alliance network',
            'Shared technology, basing, standards, financial systems, defence pooling.',
            'Coordination failures, free-riding, divergent threat perceptions.']]},
 {'k': 'section', 'num': 'Section 11', 'title': 'Geopolitics (II) — The Ruler Is a Weapon'},
 {'k': 'lede',
  't': '<i>Which ruler you choose is itself a claim about the world, and the great powers choose accordingly.</i>'},
 {'k': 'p',
  't': 'By now the two-rulers point should feel less like methodology and more like contested ground — because it '
       'is. Beijing prefers PPP: on that ruler China is already the world\'s largest economy, the "East is rising" '
       'narrative writes itself, and the implied demand for a larger voice in the institutions of the world order '
       'follows. Washington prefers nominal: on that ruler the United States still leads, the dollar system is the '
       'proof, and "America is not in decline, its allies are" is the natural reading. Neither is lying. Each has '
       'simply selected the instrument that frames the contest in its favour. A reader who can spot which ruler a '
       'pundit reached for can usually infer the argument before it is made.'},
 {'k': 'p',
  't': '<b>The dollar is the hidden denominator.</b> There is a deeper asymmetry buried in the nominal ruler, the '
       "mirror image of the PPP point about China. Every other country's nominal share is measured in the unit the "
       'United States prints. That confers a quiet flattery — reserve-currency demand and high domestic prices '
       'inflate the measured dollar value of US output — and, more importantly, a structural option no one else '
       'holds: when a global crisis hits, capital flees to the dollar, so the US share tends to rise exactly when '
       'the world is most frightened. The euro has no such put; the yuan, with a closed capital account, is nowhere '
       'near acquiring one. A structurally weaker dollar — from twin deficits, debt monetisation, or a serious move '
       "away from dollar reserves — would lower the US nominal share and lift everyone else's without a single real "
       'change in output, just as a strong dollar has flattered it. But the data counsel patience with the '
       'de-dollarisation story: the dollar is still around 58% of global reserves, no rival is close, and the yuan '
       'sits below 3%. It is a slow tail risk, not a base case — the reserve term decays in decades, not years.'},
 {'k': 'p',
  't': 'It is worth being blunt about what the nominal ruler is and is not, because the temptation is to treat it as '
       'the vain twin of "real" PPP. It isn\'t. The desk that trades these numbers keeps having to make the same '
       'four corrections.'},
 {'k': 'table',
  'headers': ['The correction', 'Why it bites'],
  'rows': [["Nominal strength isn't vanity.",
            'Dollar-priced output is what buys imports, services foreign debt, anchors reserves, and funds the '
            'institutions that turn weight into the ability to act.'],
           ["Currency weakness isn't mere optics.",
            "A softer yen, euro, or yuan really does shrink a country's dollar share and its command over traded "
            'goods — even with flat real output at home.'],
           ['PPP is not an exchange-rate forecast.',
            'It says nothing about where a currency should trade tomorrow, and should never be a standalone '
            'valuation signal.'],
           ['Sanctions and capital controls split the two rulers.',
            'An economy can hold real domestic capacity on PPP and still be locked out of the foreign technology, '
            'finance, and settlement systems only nominal dollars reach. The 2022 reserve freeze is the worked '
            "example: Russia's PPP output was untouched; its access to that output's dollar value was not."]]},
 {'k': 'p',
  't': '"Friend-shoring," trade blocs, and the weaponisation of finance — sanctions, the 2022 reserve freeze — are '
       'all attempts to manage the apparatus that converts standing into power, and all of them, pushed far enough, '
       'fragment the single world economy whose "shares" this essay has been measuring. A fragmented world does not '
       'have one GDP pie to slice; it has two or three, measured in rival units. That is the scenario the futures '
       'section prices.'},
 {'k': 'section', 'num': 'Section 12', 'title': 'The Convergence Clock'},
 {'k': 'lede',
  't': '<i>Does the gap between the two rulers stay fixed? It does not — and the way it moves is the most useful '
       'forward-looking idea here.</i>'},
 {'k': 'p',
  't': 'The mechanism has a name, the <b>Balassa–Samuelson effect</b>, and the intuition is simple. Poor, '
       'fast-growing economies have cheap non-tradable services — the haircut, the bus ride, the meal — so their PPP '
       'output looks much larger than their nominal output (China: 19.7% PPP versus 17.2% nominal; India: 8.4% '
       'versus 3.6%). As they get richer, productivity in their tradable sectors rises, wages rise across the whole '
       'economy, and the price level rises with them — so their nominal share climbs toward their PPP share. The gap '
       'between the two rulers, in other words, is a clock: it measures how far a country still has to travel.'},
 {'k': 'p',
  't': "This reframes the essay's ending. For a converging economy the gap closes from below as prosperity rises — "
       "China's nominal share will drift up toward its PPP share over the coming decades even on unchanged real "
       "growth, simply from price-level convergence; India's gap, wider still, is a longer clock with more to run. "
       'But the clock can also stall: if productivity growth stops — the middle-income trap, the fate that caught '
       'much of Latin America and arguably now Italy — the price level stops rising and the nominal share plateaus '
       "permanently below the PPP share. So the gap is both a promise and a warning. China's fork is exactly here: "
       'glide toward the frontier, or stall at the institutional ceiling a cyclical historian like Ibn Khaldun would '
       'say has caught every over-extended bureaucratic empire before it.'},
 {'k': 'fig',
  'key': 'swing24',
  'num': 'Fig. 14',
  'title': 'Why India is the swing variable',
  'sub': '',
  'caption': 'Implied PPP share of world GDP if 2024 population is held fixed and the multiplier is swept; dots mark '
             "each economy's 2024 position."},
 {'k': 'p',
  't': 'Two structural forces set the pace of that clock. The first is <b>demography</b>, and here the contrast is '
       'stark. China, Europe, Japan, and South Korea are aging and beginning to shrink — a falling working-age share '
       'is a headwind on both growth and the multiplier. India has a young and still-growing workforce: its '
       'demographic dividend is the wind at its back, which is why even modest per-head gains, multiplied across 18% '
       "of humanity, move the whole world pie. Each line in Figure 14 holds an economy's population share fixed and "
       'sweeps only its multiplier, so the steepness of the line is the population base. India and China have far '
       'the steepest slopes — roughly a sixth of humanity each — so a one-point gain in the multiplier adds about 18 '
       'points of world share for either, against barely 4 for the United States on a twentieth of the people. What '
       'makes India specifically the swing variable is where it starts: at 0.46× it has the most room to climb, and '
       'a young workforce to climb with, while China at 1.13× has already reached the middle and is aging. Lift '
       'India from 0.46× to merely the world average and its share roughly doubles, from ~8% toward ~18% — the '
       'single largest latent move on the board.'},
 {'k': 'p',
  't': "The second force is the one this essay — like Kotkin's omission of India — has itself under-weighted until "
       'now: <b>Africa and the rest of the world.</b> The grey "Rest of World" band in Figure 02 is already over a '
       "third of global output and the fastest-growing segment; sub-Saharan Africa will supply most of the planet's "
       'population growth this century, and by 2050 roughly one in four people on earth will be African. The next '
       '"missing giant," the India of the 2050s, is being born there now. An essay that measured the weight of '
       'nations and stopped at the seven Kotkin named would repeat the very omission it set out to correct.'},
 {'k': 'section', 'num': 'Section 13', 'title': 'Technology — The Engine Under the Numbers'},
 {'k': 'lede',
  't': '<i>Return to the variable everything reduced to: productivity, the third term in the identity.</i>'},
 {'k': 'p',
  't': 'The deep history of productivity is, at bottom, the history of one thing: how much energy a society can '
       "harness through knowledge and convert into useful work per pair of hands. That is the thread tying Bairoch's "
       "eighteenth-century weaver to the data centre. Britain's leap was not more weavers; it was coal and steam "
       'doing the work of millions of them. The multiplier the United States has held for 150 years is not American '
       'virtue; it is the compounding of successive general-purpose technologies, each a new way of turning energy '
       'and information into output.'},
 {'k': 'p',
  't': 'Read the long arc as a relay of these technologies. <b>Steam</b> (c. 1780–1840) broke the link between '
       'muscle and output and gave Britain its manufacturing surge. <b>Electricity and the internal-combustion '
       'engine</b> (c. 1880–1940) handed the frontier to the United States and Germany — precisely when the US '
       'multiplier vaults above 4. <b>Information and communications technology</b> (c. 1970–2010) extended the '
       'American lead into software and finance and helped open the door for the East-Asian export model. Each wave '
       'widened the gap between the societies at the frontier and everyone else; the Great Divergence is, in this '
       'light, simply the first time one civilisation pulled decisively ahead on energy-per-person and stayed there. '
       "China's recent climb is the mirror image: the fastest adoption in history of technologies the frontier had "
       'already built.'},
 {'k': 'table',
  'headers': ['Technology layer', 'GDP-share implication'],
  'rows': [['Steam, coal, factories', 'Broke the agrarian population-output link and drove the Western surge.'],
           ['Railways, electricity, mass production',
            'Created national markets, scale economies, and high industrial multipliers.'],
           ['Computers, internet, platforms',
            'Helped the US retain nominal and productivity weight while Europe and Japan lost relative share.'],
           ['Advanced manufacturing and supply chains',
            'Enabled China to convert population into industrial scale with exceptional speed.'],
           ['AI, chips, data centres, robotics',
            'Could re-concentrate frontier productivity or diffuse multiplier gains.'],
           ['Energy transition and climate adaptation',
            'Will reshape costs, industrial locations, mineral politics, and infrastructure productivity.']]},
 {'k': 'p',
  't': 'Which sets up the live question. The next general-purpose technology — artificial intelligence, layered on '
       'cheap electricity — could push the frontier in either of two opposite directions, and the honest position is '
       'that we do not yet know which. If AI mostly raises the frontier, compounding fastest where capital, data, '
       'and elite talent already cluster, it will widen the US and Chinese multipliers and re-diverge the world. If '
       'instead it diffuses fast and cheap — a tutor, a doctor, an engineer in every phone — it becomes the greatest '
       "catch-up accelerant ever built, lifting India's and Africa's multipliers toward the mean. The same "
       'technology, two vectors. Whichever wins will move these charts more than any demographic trend, because it '
       'acts directly on the only term that matters. Technology is not a miracle word: it changes GDP share only '
       'when it changes output per person at scale. Chips without electricity, factories without logistics, or AI '
       'without institutions do not automatically become national power.'},
 {'k': 'section', 'num': 'Section 14', 'title': 'The Future — Three Futures, and What to Watch'},
 {'k': 'lede', 't': '<i>No honest version of this subject ends in a forecast line.</i>'},
 {'k': 'p',
  't': 'The distribution of future shares is fat-tailed and asymmetric: the modal path is slow convergence, but the '
       'tails — a dollar crisis, a yuan float, a war over Taiwan, an AI-productivity discontinuity — are violent and '
       'would dominate everything. So the essay ends not with a prediction but with a cone: three regimes, each '
       'internally coherent, with the signals that would tell you which one you are living in.'},
 {'k': 'p',
  't': "<b>Convergence — the modal path.</b> China's nominal share drifts up toward its PPP share as its price level "
       "rises; India's wider gap slowly narrows; the US nominal share eases toward the low-20s as the dollar "
       'normalises; the West bloc keeps gently sliding. The world of 2050 is multipolar but still integrated — one '
       "pie, more evenly cut. <i>Watch:</i> yuan policy; US inflation versus trading partners; India's GDP-per-head "
       'breaking above ~$5,000.'},
 {'k': 'p',
  't': '<b>Fragmentation — the bloc path.</b> Trade blocs harden, friend-shoring deepens, reserves diversify, and '
       'the single world economy splits into rival currency-and-supply spheres. "World GDP share" becomes a '
       'contested statistic measured in different units — the question itself fractures. <i>Watch:</i> tariff and '
       "export-control regimes; the dollar's reserve share; the build-out of non-dollar payment rails."},
 {'k': 'p',
  't': '<b>Frontier discontinuity — the fat tail.</b> An AI-plus-energy productivity jump concentrates gains where '
       'capital, compute, and talent already cluster — the US and China — widening multipliers and re-diverging a '
       'world that had been converging. Size matters less than ever; the frontier matters more. <i>Watch:</i> '
       'productivity-growth data; compute and electricity build-out; whether AI gains diffuse or concentrate.'},
 {'k': 'p',
  't': 'All three turn on the same hinge — productivity, and specifically who commands the energy-and-knowledge '
       'frontier. That is the thesis returning as a forecast: population set the stage and the ruler sets the '
       'framing, but it is the third term, productivity, that decides which of these worlds we wake up in.'},
 {'k': 'table',
  'headers': ['Force', 'If it goes well', 'If it goes badly', 'Most exposed'],
  'rows': [['Demography',
            'Young workforces in India and the Global South become productive labour.',
            'Aging shrinks the working-age share in China, Europe, Japan, Russia.',
            'India · China · EU · Japan'],
           ['Technology &amp; AI',
            'Gains diffuse — a tutor, a clinician, an engineer in every phone.',
            'Gains stay narrow; valuations correct; compute and power bottlenecks bind.',
            'US · China · India'],
           ['Energy',
            'Cheap, clean electricity lowers the cost of making everything.',
            'Price shocks, climate damage, mineral chokepoints raise costs and split supply chains.',
            'EU · China · India'],
           ['Institutions',
            'States discipline incumbents, reward merit, build human capital.',
            'Middle-income traps, elite capture, polarisation stall convergence.',
            'China · India · US'],
           ['The dollar cycle',
            'Stable currencies and deep markets support nominal share and import power.',
            'Strong-dollar stress, debt strain, or fragmentation prise nominal apart from PPP.',
            'Emerging markets · euro area · Japan']]},
 {'k': 'p',
  't': 'The three middle rows act directly on productivity; the two outer ones set the headcount and move the '
       'nominal ruler. That is why the middle decides more than the edges.'},
 {'k': 'section', 'num': 'Section 15', 'title': 'The Actors, One by One'},
 {'k': 'lede', 't': '<i>Six readings off the same two rulers, each read through share, ruler, and multiplier.</i>'},
 {'k': 'country',
  'items': [('United States',
             '26.3% nominal · 15.1% PPP · 4.2% of people · ×6.2 / ×3.6',
             'The anomaly the whole essay keeps circling. America holds about a quarter of world output at market '
             'rates on roughly one twenty-fifth of its people, and it is the one rich economy that did not cede '
             'ground as China rose. None of that is a population story; it is the compounding of a century and a '
             'half at the energy-and-knowledge frontier, plus the quiet flattery of pricing the world in the unit '
             'you print. Its forward question is whether the next general-purpose technology keeps lifting US '
             'productivity, or whether fiscal strain and a narrowing of the gains hollow the multiplier out while '
             'the dollar still says otherwise.'),
            ('China',
             '17.2% nominal · 19.7% PPP · 17.5% of people · ×0.98 / ×1.13',
             'The only major economy that changes sides of the parity line depending on the ruler. Its PPP output is '
             'now the largest on earth, and its climb from a 0.2 multiplier to 1.1 is the largest movement of people '
             "toward the world's middle in recorded history; but 1.1 is the middle, not the frontier. China has done "
             'the hard part of scale — industrial depth, infrastructure, a market large enough to set world prices — '
             'and now meets the part the curves have always punished: turning catch-up into frontier productivity '
             'before aging, debt, and a closed capital account close the window.'),
            ('India',
             '3.6% nominal · 8.4% PPP · 18.0% of people · ×0.20 / ×0.46',
             'Not a small economy — a very large one with a low floor. India already holds more than a sixth of '
             'humanity and more than a twelfth of world output on PPP, yet sits below half the world average per '
             'person, a clear stage behind China on every ruler. That gap is precisely why it is the wildcard: with '
             'a base this large, even a modest rise in output per head moves the whole world pie, and its young '
             'workforce is the demographic wind no aging giant has. Whether that potential becomes weight turns on '
             'the unglamorous machinery of productivity — human capital, reliable power, female labour-force '
             'participation, manufacturing depth — not on the headcount it already holds.'),
            ('Europe + the UK',
             '21.3% nominal · 16.5% PPP · 6.5% of people · ×3.2 / ×2.6',
             'Rich, not poor, and smaller in relative share than the nominal charts of the 1990s suggest. The bloc '
             'still runs a PPP multiplier above 2.5, with deep human capital, advanced manufacturing, and regulatory '
             'reach; what it lacks is the population weight of a continental rival and the frontier-scale technology '
             "firms that let the United States convert size into platforms. Most of the West's lost share was paid "
             'here, not in Washington. Its forward question is whether an aging, fragmented bloc can organise its '
             'latent capacity — in defence, energy, and digital — into renewed productivity, or settle into a '
             'dignified plateau.'),
            ('Japan',
             '3.7% nominal · 3.4% PPP · 1.5% of people · ×2.4 / ×2.2',
             'The warning label of the whole debate, and it should be taught as one. The famous fall "from 18% to '
             '4%" is almost entirely a nominal-ruler story — the 1990s super-yen and asset bubble unwinding, plus '
             "slow growth — and Japan's PPP share never resembled that mountain. Strip the currency away and what "
             'remains is an advanced, high-multiplier economy that stopped growing its share, not a collapse.'),
            ('Russia',
             '2.0% nominal · 3.6% PPP · 1.8% of people · ×1.10 / ×2.00',
             'The reminder that GDP share bounds power without defining it. Russia looks markedly larger on PPP than '
             'nominal — cheap domestic prices nearly double its multiplier — which is the right ruler for soldiers, '
             'fuel, and steel paid for at home, and the wrong one for imported chips, jet engines, and dollar '
             'finance, which arrive at world prices a sanctioned economy cannot dodge. Its weight on the page is '
             'small; its capacity to impose costs, through energy, nuclear arms, and territorial depth, is not. It '
             'is the case where the two rulers split not by accident but by policy.')]},
 {'k': 'section', 'num': 'Section 16', 'title': 'Stepping Back — The Size of the Whole'},
 {'k': 'lede',
  't': '<i>Every share in this essay is a slice of something; before the last word, weigh the whole.</i>'},
 {'k': 'fig',
  'key': 'world_long',
  'num': 'Fig. 15',
  'title': 'Five centuries of the whole: headcount and real output, 1500–2000',
  'sub': '',
  'caption': 'Constant 2011 international dollars, PPP; deliberately not spliced to the current-dollar totals.'},
 {'k': 'fig',
  'key': 'world_modern',
  'num': 'Fig. 16',
  'title': 'The modern totals, and the road to 2050',
  'sub': '',
  'caption': "World population 1900–2024 with the UN's median projection; world GDP at current prices, nominal and "
             'PPP. Current-dollar terms, a different lane from Figure 15.'},
 {'k': 'p',
  't': 'World output in 2024 was about $110 trillion at market exchange rates, and roughly $195 trillion at '
       'purchasing-power parity in current international dollars — the same two rulers, now laid against the planet. '
       "About 8.2 billion people produced it. On the IMF's April 2026 path both totals rise further, toward roughly "
       '<b>$126 trillion nominal and $223 trillion PPP</b> for 2026. Population climbed from about 1.65 billion in '
       '1900 to 8.2 billion in 2024 and is projected near 9.7 billion by 2050, peaking around 10.3 billion in the '
       '2080s before turning down. Most of the growth still to come is African — the next missing giant, being born '
       "where the essay's demography pointed."},
 {'k': 'p',
  't': 'Hold the two pictures together and the claim is visible in one sweep. Across five centuries the headcount '
       'rose roughly fourteenfold; real output rose more than a hundredfold. Output ran far ahead of population, and '
       'the widening gap between the bars and the line is output per person — the productivity term from the '
       'identity, almost all of it earned in the last two centuries. The shares are how the pie is cut; the totals '
       'are how much there is to cut, and how fast it is still growing.'},
 {'k': 'section', 'num': 'Section 17', 'title': 'Claim Audit'},
 {'k': 'lede',
  't': "<i>A useful soundbite is a ruler-labelled soundbite. Most of Kotkin's claims are directionally right; they "
       'go wrong only when the ruler is left unnamed and a PPP fact is read as a nominal one, or vice versa.</i>'},
 {'k': 'table',
  'headers': ['His claim', 'Ruler', 'Verdict &amp; the figures'],
  'rows': [['US ≈ 25% of world GDP since ~1880',
            'Nominal',
            '<b>Holds.</b> Long-run average near a quarter; ~26% nominal in 2024, ~15% on PPP. The 2011 trough was '
            '~21–23%, and the line has recovered since.'],
           ['Postwar peak ~50% was the anomaly',
            'Both',
            '<b>Holds — and is more ruler-dependent than it sounds.</b> ~50% nominal in 1945 (a rubble artifact), '
            '~40% by 1960, but only ~27% on PPP around 1950. The "anomaly" framing is exactly right.'],
           ['Japan: ~18% → ~4%',
            'Nominal',
            '<b>Holds.</b> Peak ~18% in 1994 (super-yen + bubble); ~3.7% in 2024. On PPP, Japan never exceeded ~8% — '
            'most of the "fall" is currency unwinding plus slow growth.'],
           ['Europe (incl. UK): ~30% (1992) → ~17%',
            'Mixed',
            '<b>Roughly holds, but blended.</b> The "~17%" matches PPP for Europe; nominal EU+UK today is closer to '
            '~21%. The "~30% in 1992" is nominal. Two rulers in one sentence.'],
           ['China ≈ 40% before the 1800s',
            'PPP',
            "<b>High-end estimate.</b> Maddison's GDP peak for China is closer to a third (~33% in 1820). The bigger "
            'figure is often the manufacturing share, not GDP. Contested on level and timing.'],
           ['US: 5% of population, 25% of GDP',
            'Both',
            '<b>Holds.</b> Multiplier ≈ 6 nominal, ≈ 3.6 PPP. The US is ~4.2% of world population — so the '
            'per-capita lead is, if anything, understated by "5%."'],
           ['India left out of the story',
            'PPP &amp; multiplier',
            '<b>The omission.</b> India was ~24% of world GDP in 1700, fell to ~3% nominal, and is back to ~8% PPP — '
            'yet at a multiplier of just ~0.46, a stage behind China, and the largest single swing factor on the '
            'board.'],
           ['GDP share equals power',
            'No single ruler',
            '<b>Incomplete.</b> GDP is capacity; power requires conversion through finance, technology, '
            'institutions, military logistics, energy, and alliances.']]},
 {'k': 'section', 'num': 'Section 18', 'title': 'Conclusions'},
 {'k': 'lede', 't': '<i>Seven things the numbers actually say.</i>'},
 {'k': 'conclusions',
  'items': [('Size is headcount; weight is productivity.',
             'The multiplier dissolves the myth of a "rich" pre-industrial Asia: China\'s 33% of 1820 was a 0.9× '
             'multiplier — many people at subsistence, not a wealthy society. Aggregate size has always been mostly '
             'a population story.'),
            ('The ruler must match the question.',
             'PPP for living standards, nominal for financial and geopolitical weight. Neither is "true"; the gap '
             'between them is information — and the choice of ruler is itself a move on the board.'),
            ("The US didn't decline — its allies did.",
             'America held its ~25% nominal share for four decades; Europe and Japan ceded the ground that went to '
             'China. But allied decline is a double edge: it raises relative standing while eroding the coalition '
             'that converts standing into power.'),
            ("China's rise is real in output, barely begun in prosperity.",
             'It is the largest economy on PPP and has lifted more people from poverty than any society in history — '
             'yet it only just crossed the world-average multiplier, and now faces the middle-income fork: glide to '
             'the frontier, or stall at the institutional ceiling.'),
            ('The nominal/PPP gap is a clock.',
             "By Balassa–Samuelson it closes from below as a converging economy's prices rise, and stalls if "
             "productivity growth stops. China's nominal share will drift up toward its PPP share — unless the clock "
             'stops.'),
            ('India is the wildcard; Africa is the next omission.',
             "With 18% of humanity and a 0.46× multiplier, India's modest per-head gains move the whole pie. And the "
             '"Rest of World" — already over a third of output, Africa above all — is where the missing giant of '
             '2050 is being born.'),
            ('The frontier decides the future.',
             'Every path turns on productivity, and productivity now means energy and AI. The next rebalancing will '
             'be settled by knowledge and power, not headcount — and it should be read with humility, because the '
             'rulers themselves are wobbly to ±5–10%.')]},
 {'k': 'p',
  't': 'The final answer is not "America is declining" or "China is replacing America." It is sharper: America '
       'remains a high-multiplier, high-nominal-weight economy; China has become the largest real-output aggregate '
       'in PPP terms but still sits near the world average per person; India is the biggest under-discussed swing '
       'factor; Europe and Japan are rich but smaller in relative share; and the next era will be decided by '
       'technology diffusion, institutions, energy, demographics, and the political ability to turn output into '
       'power. Which side of the world average the largest society on earth comes to rest on — and who, in the next '
       'decade, gets to decide — no ruler can tell you. Only its people can, with whatever they are allowed to make '
       'of their days.'},
 {'k': 'section', 'num': 'The Long View', 'title': 'Scenarios and Implications to 2050'},
 {'k': 'lede',
  't': '<i>A speculative extension — more exploratory than the essay above, and held to a lower evidentiary bar on '
       'purpose. It was developed through three panels run in designed disagreement, five rounds each: a '
       '<b>deep-thinkers</b> roundtable for the structural and civilizational analysis (with Ibn Khaldun, Sun Tzu, '
       'Rachel Carson, and Hannah Arendt called in), an <b>fx-experts</b> assessment for the monetary-order '
       'trajectory (its Turkish-lira brief adapted to the global reserve-currency question), and a '
       '<b>wisepersons</b> panel for the epistemic and ethical frame (Haraway, Morrison, Kahle, adapted from their '
       'native domain). What follows is the synthesis; the dialogue is not printed. Read it for shape and stakes, '
       'not as forecast — the rulers are wobbly to ±5–10%, the horizon is far, and the discontinuities at the end of '
       'this part would overwrite any baseline drawn before them.</i>'},
 {'k': 'p',
  't': 'The essay proper ended at a wall it would not climb: which way the slices move next, no ruler can tell you. '
       'This part climbs the wall anyway, with the humility the height demands. It does not predict 2050. It maps '
       'the space of credible 2050s, names the forces that select among them, and asks the questions the bare shares '
       'cannot — for whom each future is good, who gets to author it, and what survives if the system it assumes '
       'breaks.'},
 {'k': 'h3', 't': 'The Four Drivers — And the Fifth That Cuts Across'},
 {'k': 'p',
  't': 'Twenty-four years is not long. Much of 2050 is already determined: the workers of 2050 are alive now, the '
       'capital stock turns over slowly, and institutions change at the pace of generations. So the panels began by '
       'separating what is nearly fixed from what is genuinely open, and four drivers survived as the levers that '
       'will select which future arrives.'},
 {'k': 'p',
  't': '<b>Productivity — the AI-and-energy question.</b> This is the only term that compounds, and the one true '
       'wildcard. The next general-purpose technology, artificial intelligence layered on cheap electricity, will '
       'either raise the frontier where capital, compute, and talent already cluster, or diffuse cheaply into every '
       'phone and clinic. Nothing else on this list moves the multiplier as far or as fast.'},
 {'k': 'p',
  't': '<b>The monetary order — the dollar question.</b> Whether the dollar-centric system holds, erodes gently, or '
       'fragments into rival currency spheres governs the <i>nominal</i> ruler — financial command, the ability to '
       'borrow, sanction, and settle — independent of who produces the most real output. A country can lead in PPP '
       'volume and still be locked out of the systems only dollars reach.'},
 {'k': 'p',
  't': '<b>Demography — the most predictable driver.</b> The working-age wave is already cast. India and sub-Saharan '
       'Africa carry a young, growing labour force; China, Europe, Japan, and Korea are aging and beginning to '
       'shrink. Demography rarely decides the winner, but it sets the tailwinds and headwinds everyone else must '
       'work against.'},
 {'k': 'p',
  't': "<b>Institutional vitality — the Ibn Khaldun driver.</b> The least visible and, the panel's sharpest voice "
       'argued, the most decisive over decades. The middle-income trap, elite capture, fiscal indiscipline, the slow '
       'ossification of the institutions that built a boom — these are what stall a converging economy or hollow a '
       'frontier one. The deepest risk to both the United States and China is internal, not the rise of the other.'},
 {'k': 'fig',
  'key': 'demography',
  'num': 'Fig. 20',
  'title': 'Demographic destiny: working-age (15–64) population, indexed to 2024 = 100, projected to 2050',
  'sub': 'Projection · UN WPP 2024 (medium variant)',
  'caption': 'Diverging lines: sub-Saharan Africa and India climbing steeply, the United States roughly flat, China '
             'and Europe declining, Japan falling fastest. The one driver the chart can state with near-certainty, '
             'because its 2050 cohort is already born.'},
 {'k': 'p',
  't': 'Cutting across all four is <b>energy and ecology</b> — not a side-constraint but a primary force. The cost '
       'of decarbonised power and the politics of critical minerals will reshape where things are made; a serious '
       'climate shock or a minerals-supply rupture is a live tail. Cheap clean electricity lowers the cost of making '
       'everything and is the substrate AI runs on; expensive or contested energy raises every other cost and splits '
       'supply chains. Energy is the medium in which the other four drivers act.'},
 {'k': 'h3', 't': 'The Scenario Space'},
 {'k': 'p',
  't': 'Two of the four drivers are both high-impact and genuinely uncertain — the <i>frontier</i> (does '
       'AI-and-energy concentrate productivity or diffuse it?) and the <i>order</i> (does the global system '
       'integrate or fragment?). Crossed, they generate four coherent worlds. A fifth, the stagnation baseline, is '
       'orthogonal: it is what any of the four becomes if productivity simply disappoints. Demography and '
       'institutions then determine <i>who</i> occupies which position within each world.'},
 {'k': 'fig',
  'key': 'scenario_space',
  'num': 'Fig. 17',
  'title': 'The scenario space',
  'sub': 'Conceptual map — not a data plot',
  'caption': 'A 2×2: the horizontal axis runs from the frontier <i>concentrating</i> (left) to <i>diffusing</i> '
             '(right); the vertical axis from the order <i>fragmenting</i> (bottom) to <i>integrating</i> (top). The '
             'four quadrants are named below; a fifth scenario, the Long Plateau, sits across the centre as the '
             'low-productivity version of all four.'},
 {'k': 'p',
  't': '<b>Frontier Pull-Away</b> <i>(integrated order, concentrated frontier).</i> One world market, but '
       'AI-and-energy gains compound where they already cluster — the United States, China, a handful of hubs. The '
       "frontier economies' multipliers widen; the catch-up stalls; inequality between nations grows inside an "
       'integrated system. This is §14\'s "frontier discontinuity," refined: re-divergence without fragmentation. '
       'The US re-anchors on a productivity boom and the dollar with it; China holds its scale but the gap to the '
       'frontier stops closing.'},
 {'k': 'p',
  't': '<b>The Great Catch-Up</b> <i>(integrated order, diffused frontier).</i> The optimistic path. Cheap '
       'intelligence and cheap power diffuse fast — a tutor, a clinician, an engineer in every phone — and become '
       "the largest catch-up accelerant ever built. India's multiplier climbs toward and past the world average; "
       'Africa industrialises a generation faster than the historical script; the gap between nations narrows for '
       'the first time since the Great Divergence. World growth is high; the shares converge toward population '
       'weight. The world of 2050 is multipolar and richer.'},
 {'k': 'p',
  't': '<b>Two Suns</b> <i>(fragmented order, concentrated frontier).</i> The most dangerous world. The system '
       'splits into a US-led and a China-led techno-economic sphere, each with its own standards, payment rails, '
       'supply chains, and currency bloc; the frontier concentrates <i>within</i> each sphere; the unaligned — India '
       'above all, much of the Global South — hedge between them and extract rents from the rivalry. "World GDP '
       'share" stops being one statistic: there are two pies, measured in rival units, and the nominal ruler itself '
       'bifurcates.'},
 {'k': 'p',
  't': '<b>Archipelago</b> <i>(fragmented order, diffused frontier).</i> Technology diffuses, but the order '
       'fragments into several regional spheres rather than two camps. More autonomous regional economies; diffusion '
       'lifts many, but the gains from a single integrated market are lost to friction. Messy, plural multipolarity '
       '— neither the clean rivalry of Two Suns nor the open integration of the Catch-Up.'},
 {'k': 'p',
  't': '<b>The Long Plateau</b> <i>(any order, productivity disappoints).</i> The baseline the panels kept returning '
       'to as the <i>modal</i> near-term reality. AI underdelivers on measured growth; aging, debt overhangs, and '
       'middle-income traps bind; no one pulls away and no one catches up fast. Shares drift slowly, almost entirely '
       'by demography. A low-growth, multipolar, integrated-but-sluggish world — secular stagnation as the global '
       'default. Not a catastrophe; a long, grey flatness.'},
 {'k': 'fig',
  'key': 'cone',
  'num': 'Fig. 18',
  'title': 'The cone of outcomes',
  'sub': 'Illustrative scenario — not a forecast',
  'caption': 'World GDP share at PPP for the United States, China, and India, 2024 → 2050, each drawn as a shaded '
             "fan spanning the five scenarios. The fans widen with time and overlap: China's upper edge "
             "(Pull-Away/Two Suns scale) and India's upper edge (Great Catch-Up) are the widest, the United States' "
             'the narrowest — a visual statement that the most uncertain economies are the populous risers, not the '
             'incumbent.'},
 {'k': 'h3', 't': 'What Each Scenario Does to the Map'},
 {'k': 'p',
  't': 'The scenarios are not equally kind to each actor, and the same economy can be a winner in one and a casualty '
       'in another. The table reads the five worlds as rough 2050 PPP-share directions, not point forecasts — the '
       'arrows are the message.'},
 {'k': 'table',
  'headers': ['Actor', 'Frontier Pull-Away', 'Great Catch-Up', 'Two Suns', 'Archipelago', 'Long Plateau'],
  'rows': [['<b>United States</b>',
            '↑↑ re-anchors on AI productivity; dollar strong',
            '↓ relative, as others rise; richer absolutely',
            '↑ leads one sphere; financial command intact',
            '↓ one pole among several',
            '→ drifts, aging-light, holds quarter slowly'],
           ['<b>China</b>',
            '→ holds scale, gap to frontier stalls',
            '↑ converges, but aging caps it',
            '↑↑ anchors the rival sphere; most leverage',
            '↑ regional hegemon of its zone',
            '→ demography and debt bite; slow plateau'],
           ['<b>India</b>',
            '↓ left behind the frontier',
            '↑↑ the largest single gain on the board',
            '↑ the swing prize both spheres court',
            '↑ leads its own regional zone',
            '↑ slowly; demography carries it alone'],
           ['<b>Sub-Saharan Africa</b>',
            '↓↓ the omission deepens',
            '↑↑ industrialises a generation early',
            '→ courted, fragmented, hedging',
            '↑ regional integration helps',
            '→ population grows, output lags'],
           ['<b>EU + UK</b>',
            '↓ falls further behind the frontier',
            '→ holds, modernises at the margin',
            '↓ squeezed between two spheres',
            '→ a regional pole, diminished',
            '↓ aging and stagnation compound'],
           ['<b>Rest of World</b>',
            '↓ frontier rents bypass them',
            '↑ broad diffusion lifts the floor',
            '→ bloc-aligned or hedging',
            '↑ regionalism favours them',
            '→ flat']]},
 {'k': 'fig',
  'key': 'scenario_bars',
  'num': 'Fig. 19',
  'title': '2050 PPP shares under each scenario',
  'sub': 'Illustrative scenario — not a forecast',
  'caption': 'Grouped bars: the United States, China, India, sub-Saharan Africa, EU+UK, and Rest of World, shown '
             "five times across the scenarios. The eye should catch two things — how far India's and Africa's bars "
             "swing between Pull-Away and Catch-Up, and how little the United States' bar moves regardless, the "
             "incumbent's share being the most insured against the future."},
 {'k': 'h3', 't': 'The Monetary Order to 2050'},
 {'k': 'p',
  't': 'The fx-experts panel, asked to look past the lira to the system itself, returned a house view notable for '
       'its restraint: the dollar order most likely <b>persists but erodes</b>, rather than either enduring '
       "untouched or collapsing. The dollar's reserve share, having drifted from roughly 70% in 2000 to about 58% "
       'now — call it half a point a year — most plausibly reaches the mid-to-high 40s or low 50s by 2050: a more '
       'multipolar system in which the dollar remains primary because no rival combines the three things reserve '
       'status requires at once — a deep market of safe assets, an open capital account, and the rule of law — at '
       'sufficient scale. The euro lacks the unified fiscal backing; the yuan is structurally capped below 3% '
       'precisely because opening the capital account would mean surrendering the capital controls the Chinese state '
       'will not cede. The reserve role is far stickier than the de-dollarisation headlines, which mostly track '
       'bilateral <i>trade settlement</i> — small relative to reserves and capital markets — rather than the reserve '
       'and funding roles that actually confer power.'},
 {'k': 'fig',
  'key': 'dollar',
  'num': 'Fig. 21',
  'title': "The dollar's reserve share to 2050, four paths",
  'sub': 'Illustrative scenario — not a forecast',
  'caption': 'From ~58% in 2024: a <i>status-quo-plus</i> line (an AI-driven US productivity boom and safe-asset '
             'demand hold it near 55%), a <i>base drift</i> (toward ~48%), a <i>fragmentation</i> path (a rival bloc '
             'forms; toward ~40%), and a low-probability <i>rupture</i> (a disorderly fiscal-crisis repricing; a '
             'faster, steeper fall). The reserve premium can erode for decades and then break in months — the lines '
             'fan slowly, but the rupture tail is drawn for a reason.'},
 {'k': 'p',
  't': 'The asymmetry the panel kept returning to is the one the essay flagged: the dollar is a <i>crisis hedge</i>. '
       'In a global shock, capital flees toward it, so the US nominal share tends to <i>rise</i> exactly when the '
       'world is most frightened. Betting against the dollar order is, in effect, shorting a convexity that pays off '
       'in tail events — which is why the order is more durable than its critics expect and more fragile than its '
       'defenders admit. The fattening tail is <b>fragmentation as policy</b>: sanctions, export controls, and '
       'reserve freezes are actively pushing the system toward bipolarity from both sides, and a hardening into a '
       'rival settlement bloc — gold, the yuan in trade, CBDC rails for the sanctioned and the hedging — is what '
       "would move the dollar's share fastest and split the nominal ruler into two. The minority risk: a disorderly "
       'dollar repricing from twin deficits and a politicised central bank is low-probability but under-priced, and '
       'it would dominate the nominal picture overnight.'},
 {'k': 'h3', 't': 'The Frontier Question — The One Variable That Matters Most'},
 {'k': 'p',
  't': 'If only one driver could be known, the panels agreed it should be this: does the AI-and-energy frontier '
       '<b>concentrate</b> or <b>diffuse</b>? Because it acts directly on the only term that compounds, it has the '
       'widest fan of any single variable — wider than demography, wider than the dollar. The same technology runs '
       'two opposite vectors. Concentrated, it is the greatest <i>re-divergence</i> engine since coal and steam: '
       'gains compound where data, capital, and elite talent already sit, the frontier multipliers widen, and the '
       'Long Divergence gets a second act. Diffused, it is the greatest <i>convergence</i> engine ever built: the '
       'marginal cost of expertise collapses, and a clinic in Patna or Lagos gets a diagnostician, a tutor, an '
       'engineer it could never staff.'},
 {'k': 'fig',
  'key': 'multiplier_shift',
  'num': 'Fig. 22',
  'title': 'Diffuse versus concentrate, drawn on the multiplier',
  'sub': 'Illustrative scenario — not a forecast',
  'caption': 'Projected change in PPP output per head relative to the world average, 2024 → 2050, for frontier '
             'economies (United States, EU) against catch-up economies (India, sub-Saharan Africa), under the two AI '
             'vectors. Under <i>concentrate</i>, the frontier lines rise and the catch-up lines flatten — the gap '
             'widens. Under <i>diffuse</i>, the catch-up lines rise sharply and the frontier lines plateau — the gap '
             'narrows. Same technology; opposite worlds; one chart.'},
 {'k': 'p',
  't': 'Which vector wins is not purely technological. It is set by whether the gains are captured or shared — by '
       'competition policy, by who owns the compute and the models, by whether cheap power reaches the places that '
       'need it, and by the institutions that turn a tool into broad productivity. Chips without electricity, models '
       'without institutions, and intelligence without the schooling to use it do not lift a multiplier. The '
       'frontier question is, underneath, a political question wearing a technological costume.'},
 {'k': 'h3', 't': 'The Discontinuities — What Overwrites the Baseline'},
 {'k': 'p',
  't': "The scenarios above are slow-driver baselines. The panel's most insistent minority view — and the "
       "wisepersons' resilience reading — is that the <i>tails</i> carry more expected impact than the modal path, "
       'because any one of them rewrites the board faster than demography or institutions ever could. A forecast '
       'that names only the smooth paths is a forecast lying about its own confidence.'},
 {'k': 'p',
  't': 'The fat tails worth naming: a <b>war over Taiwan</b>, which would fracture the semiconductor frontier and '
       'the trade order at once and force the Two Suns world overnight; a <b>disorderly dollar repricing</b> from a '
       'US fiscal crisis or a politicised Fed; an <b>AI discontinuity</b> — a genuine jump to broadly transformative '
       'systems — that concentrates power faster than any institution can redistribute it, or, inversely, an <b>AI '
       'disappointment</b> that collapses the valuations and the growth premium the optimistic paths assume; a '
       '<b>pandemic</b> worse than the last; and a <b>climate or minerals shock</b> — a breadbasket failure, a '
       'critical-minerals chokepoint — that raises the cost of everything and splits supply chains. Each is '
       'low-probability in any given year and high-probability across a quarter-century; each would dominate the '
       "slow drivers if it landed. The honest posture is Tao's: the future of economic weight is a fat-tailed, "
       'asymmetric distribution, and the baseline is mostly a story we tell to fill the space the tails will likely '
       'overwrite.'},
 {'k': 'h3', 't': 'The Standpoint and the Stakes'},
 {'k': 'p',
  't': 'The wisepersons panel refused to let the section end as a power-ranking, and its objection is part of the '
       'finding rather than a footnote to it. Three corrections to everything above.'},
 {'k': 'p',
  't': '<b>Whose future is this, and who authored it?</b> Every scenario here is structured around the powers that '
       'already hold weight — the United States, China, India, the EU, the dollar. That is a view from the centre, '
       'written from the vantage of those who <i>measure</i> weight, and the vantage shapes which futures get '
       "imagined. The clearest symptom is the one the essay already named as Kotkin's error and then half-repeated: "
       '<b>sub-Saharan Africa</b>, which will hold roughly one in four human beings by 2050 and supply most of the '
       "planet's population growth, appears in the standard scenario literature — and nearly appeared here — as a "
       '"swing factor" and a "Rest of World" band rather than as a set of societies with futures of their own '
       'authorship. The next missing giant is being born there now, and it does not get a vote in the scenarios that '
       'describe its life. Naming this is not a caveat to the analysis; it is a correction to it.'},
 {'k': 'p',
  't': '<b>The decimal hides a person — at the horizon too.</b> "India\'s multiplier climbs to 0.7" and "Africa '
       'industrialises early" are abstractions for whether several hundred million people cross from precarity to '
       'security — whether a child gets a grid, a clinic, a school. The Great Catch-Up is not, at bottom, a '
       'redistribution of share-points; it is the largest improvement in human lives the century could contain. The '
       'Long Plateau is not a grey flatness on a chart; it is a generation in the Global South that does not get the '
       'convergence the last one was promised. The scenarios are worth ranking by that, not only by who leads.'},
 {'k': 'p',
  't': '<b>Efficiency is not resilience.</b> The macro panels optimise for <i>who will be biggest</i>; the '
       "preservationist's question is <i>what survives when the system breaks</i>. A hyper-optimised, concentrated, "
       'just-in-time global economy — the Frontier Pull-Away world — is also the most fragile to any of the '
       'discontinuities above. The resilient futures are the redundant, somewhat-localised, plural ones that trade '
       'efficiency for survivability. That efficiency-versus-resilience tradeoff is a dimension the share-charts '
       'cannot show and the next decade will keep testing — and it is, quietly, an argument that the messier '
       'Archipelago may be safer than the cleaner worlds on either side of it.'},
 {'k': 'h3', 't': 'What to Watch'},
 {'k': 'p',
  't': 'The leading indicators that tell you which way the drivers are turning — the dials to read over the next '
       'decade, organised by the driver each one tracks.'},
 {'k': 'table',
  'headers': ['Driver', 'Watch', 'A turn means'],
  'rows': [['<b>Productivity / AI</b>',
            'Measured productivity-growth data in the US and China; whether AI gains show up in output per hour '
            'broadly or only in a few firms; compute and electricity build-out',
            'Broad productivity gains → diffusion and Catch-Up; narrow gains → concentration and Pull-Away'],
           ['<b>The monetary order</b>',
            "Dollar reserve share (annual COFER); the <i>gap</i> between the yuan's trade-settlement share and its "
            'reserve share; US debt/GDP and term-premium behaviour; non-dollar rails (CIPS, mBridge, CBDCs); '
            'commodity invoicing units',
            'A closing yuan reserve gap or commodity de-dollarisation → fragmentation; a stable gap → slow drift'],
           ['<b>Demography</b>',
            "India's labour-force participation, especially female; African industrial job creation; China's and "
            "Europe's old-age dependency ratios",
            'Participation rising where the workers are → tailwinds convert to output'],
           ['<b>Institutions</b>',
            "China's response to the middle-income fork; US fiscal trajectory and institutional cohesion; reform "
            'versus capture across the Global South',
            'Reform → convergence; capture and indiscipline → stall, on the Ibn Khaldun pattern'],
           ['<b>Energy / ecology</b>',
            'The falling cost of clean electricity; critical-minerals concentration and chokepoints; climate-shock '
            'frequency',
            'Cheap diffuse power → Catch-Up substrate; contested or shocked energy → fragmentation and the tails'],
           ['<b>The swing variable</b>',
            "India's GDP per head crossing ~$5,000; sub-Saharan Africa's manufacturing share beginning to rise",
            'The single largest latent move on the board beginning to cash']]},
 {'k': 'h3', 't': 'Closing the Long View'},
 {'k': 'p',
  't': 'Strip the five worlds and the six dials down, and the same hinge that ran through the essay runs through its '
       'future: <b>productivity</b> — and specifically whoever commands the energy-and-knowledge frontier, and '
       'whether they hoard it or share it. Population set the stage and the ruler set the framing, but the third '
       'term decides which 2050 we wake up in. The modal near-term path is a muddle — the frontier pulling away '
       'somewhat while growth stays mediocre, with fragmentation a rising probability and the tails fattening '
       'underneath. The most leveraged unknown is the AI vector; the most decisive slow risk is internal — '
       'legitimacy and discipline, in Washington and Beijing alike; and the most under-counted actors are the '
       'African societies the maps keep drawing as a residual.'},
 {'k': 'p',
  't': 'And the part the rulers will never measure stays exactly where the essay left it. Whether the next '
       'quarter-century is the Great Catch-Up or the Long Plateau is not, finally, a fact waiting in the data. It is '
       'something hundreds of millions of people will make, or be prevented from making, out of whatever they are '
       'given and whatever they are allowed. The charts can show you the shape of the room. They cannot tell you '
       'what the people in it will choose to build — only that, this time, far more of them will be in a position to '
       'choose.'},
 {'k': 'section', 'num': 'Appendix A', 'title': 'Data &amp; Methodology'},
 {'k': 'lede', 't': '<i>Three source lanes, kept deliberately un-stitched.</i>'},
 {'k': 'p',
  't': 'This report uses several source lanes and keeps them separate by design. The long-run historical view is '
       'Maddison-style; the modern 1990–2024 view is World Bank WDI variables (as carried through the QoG standard '
       'country-year file); the present-day marker is the IMF WEO April 2026 vintage. They are related, but they are '
       'not one seamless instrument.'},
 {'k': 'p',
  't': 'The core calculations are simple. GDP share is entity GDP divided by world-country-sum GDP under the chosen '
       'ruler. Population share is entity population divided by world-country-sum population. The multiplier is GDP '
       'share divided by population share — 1.0 means world-average output per person; 4.0 means roughly four times '
       'the world average.'},
 {'k': 'table',
  'headers': ['Lane', 'Used for', 'Main caveat'],
  'rows': [['Maddison Project Database (Bolt &amp; van Zanden, 2023 update)',
            '1500–2008 benchmark shares and long-run multipliers; folds in Bassino &amp; van der Eng and Ma &amp; de '
            'Jong East-Asia studies.',
            'Historical borders, PPP benchmarks, sparse data, reconstruction uncertainty. The workbook effectively '
            'ends ~2008.'],
           ['World Bank WDI / QoG modern country-year file',
            '1990–2024 nominal shares, PPP shares, population shares, and multipliers.',
            'Country-sum denominators and variable definitions can differ from official IMF/global aggregates by a '
            'few tenths of a point.'],
           ['IMF WEO April 2026 marker',
            'Current projection marker for nominal GDP, PPP GDP, PPP shares, and macro aggregates.',
            'A projection vintage; not spliced backward into historical series.'],
           ['UN World Population Prospects 2024',
            'World population and projections to 2050/2100, anchoring the multiplier denominator.',
            'Medium-variant demographic projection; not an economic forecast.'],
           ['Bairoch-style manufacturing series',
            'Industrial-power context during the Great Divergence.',
            'Approximate historical manufacturing shares; used for direction, not decimals.']]},
 {'k': 'p',
  't': '<b>Why not stitch everything into one continuous 1500–2026 line?</b> Because the appearance of continuity '
       'would be false precision. Long-run Maddison reconstructions, WDI modern PPP series, and IMF projection '
       'markers use different vintages, benchmark systems, and assumptions. A visually smooth line would look more '
       'scientific while being less honest. The deeper into the past a chart reaches, the more its decimal point is '
       'a costume.'},
 {'k': 'p',
  't': '<b>On the three PPP totals.</b> World PPP GDP appears in three forms in this report, deliberately '
       'distinguished: <b>$222.8 trillion</b> (IMF April 2026, 2026 projection, current international dollars — the '
       'present-day marker); <b>~$195 trillion</b> (2024, current international dollars — the modern snapshot); and '
       '<b>~$170 trillion</b> (2024, WDI constant 2021 international dollars — the internal real-output arithmetic). '
       'They are not interchangeable, and the figures are not averaged across lanes.'},
 {'k': 'p',
  't': '<b>Uncertainty discipline.</b> Pre-1900 numbers are reconstructed estimates with wide error bars. Modern '
       'numbers are more precise but still depend on ruler, denominator, source vintage, and grouping. PPP itself '
       'carries ±5–10% structural uncertainty and has lurched by tens of percent for China across ICP rounds. Future '
       'numbers are scenarios, not forecast certainties.'},
 {'k': 'section', 'num': 'Appendix B', 'title': 'The Reference Tables'},
 {'k': 'lede', 't': '<i>The numbers under the charts, gathered in one place so the figures can be reproduced.</i>'},
 {'k': 'p',
  't': '<b>B1 — World GDP, two rulers and two multipliers, 2024 (WDI country-sum).</b> Shares against a world total '
       'of roughly $110T nominal / ~$170T PPP (constant 2021 int\\$, ≈$195T current); they differ by a few tenths '
       'from aggregations built on official world totals. EU-27 + UK is a constructed sum. The decimals are '
       'calculation artifacts — read the ruler, the order of magnitude, and the gap.'},
 {'k': 'table',
  'headers': ['Entity', 'Nominal %', 'PPP %', 'Population %', 'Nominal ×', 'PPP ×'],
  'rows': [['United States', '26.34', '15.07', '4.23', '6.23', '3.56'],
           ['China', '17.17', '19.72', '17.51', '0.98', '1.13'],
           ['EU-27', '17.88', '14.36', '5.59', '3.20', '2.57'],
           ['EU-27 + UK', '21.25', '16.49', '6.45', '3.29', '2.56'],
           ['United Kingdom', '3.38', '2.14', '0.86', '3.93', '2.48'],
           ['India', '3.58', '8.36', '18.03', '0.20', '0.46'],
           ['Japan', '3.69', '3.35', '1.54', '2.40', '2.18'],
           ['Russia', '1.96', '3.57', '1.78', '1.10', '2.00']]},
 {'k': 'p',
  't': '<b>B2 — The IMF April 2026 current marker.</b> Kept on its own page and deliberately not stitched into the '
       'long-run series (different vintage, different benchmark system). World totals: nominal <b>$126.3T</b>; PPP '
       '<b>$222.8T</b>, both in current dollars / current international dollars. Nominal shares computed against the '
       '$126.3T world total; EU + UK is a constructed sum.'},
 {'k': 'table',
  'headers': ['Entity', 'IMF PPP share %', 'Nominal GDP ($tn)', 'Nominal share %'],
  'rows': [['United States', '14.54', '32.38', '25.64'],
           ['China', '19.89', '20.85', '16.51'],
           ['India', '8.49', '4.15', '3.29'],
           ['European Union', '13.77', '23.03', '18.23'],
           ['EU + UK', '15.89', '27.30', '21.62'],
           ['United Kingdom', '2.12', '4.26', '3.37'],
           ['Japan', '3.26', '4.38', '3.47'],
           ['Russia', '3.38', '2.66', '2.11']]},
 {'k': 'p',
  't': '<i>How to use the marker: the IMF row is a current projection snapshot — world prices, current exchange '
       "rates, current international-dollar PPP. The WDI/QoG country-sum table (B1) carries the report's internal "
       '2024 share and multiplier arithmetic. Maddison-style data carries the centuries. The lanes touch, but they '
       'are not the same road.</i>'},
 {'k': 'p', 't': '<b>B3 — The centuries, in one table (Maddison-style, 1990 international dollars).</b>'},
 {'k': 'table',
  'headers': ['Year', 'Population', 'World PPP output', 'Output per person', 'Reading'],
  'rows': [['1500', '~0.44bn', '$0.25T', '~$565', 'Agrarian scale: output mostly follows people, land, calories.'],
           ['1700',
            '~0.60bn',
            '$0.37T',
            '~$615',
            'Still a population-weighted world; China and India remain huge in aggregate.'],
           ['1820',
            '~1.04bn',
            '$0.69T',
            '~$665',
            'Industrial divergence beginning; old agrarian weights still visible.'],
           ['1870',
            '~1.27bn',
            '$1.11T',
            '~$870',
            'Steam, coal, railways, finance begin to widen the per-person gap.'],
           ['1913', '~1.79bn', '$2.73T', '~$1,525', 'Before WWI, industrial output has remade the economic map.'],
           ['1950',
            '~2.53bn',
            '$5.34T',
            '~$2,110',
            'The postwar American peak sits inside a world still rebuilding.'],
           ['1973',
            '~3.92bn',
            '$16.02T',
            '~$4,090',
            'Postwar growth multiplies world output faster than population.'],
           ['2000',
            '~6.15bn',
            '$36.69T',
            '~$5,970',
            'Globalisation raises scale; China and India re-enter modern production.'],
           ['2008', '~6.71bn', '$50.97T', '~$7,600', 'End of the Maddison long-run GDP lane used here.']]},
 {'k': 'p',
  't': '<i>Modern totals (2024: ~$110T nominal current US\\$; ~$195T PPP current int\\$; ~$170T PPP constant-2021 '
       'int\\$) use different statistical lanes and are not spliced onto this scale.</i>'},
 {'k': 'section', 'num': 'Appendix C', 'title': 'Bibliography &amp; Data-Source Urls'},
 {'k': 'lede',
  't': '<i>Sources used for definitions, data lanes, and the inspiration reference. The data essay avoids full '
       'academic footnoting in the body to stay readable; this appendix and the build bundle are the audit '
       'trail.</i>'},
 {'k': 'table',
  'headers': ['Resource', 'URL / identifier', 'Used for'],
  'rows': [['Hoover inspiration',
            'youtube.com/watch?v=gBEdxb8ei_0',
            'User-specified source: <i>Uncommon Knowledge</i>, Hoover Institution; guest Stephen Kotkin, host Peter '
            'Robinson.'],
           ['Hoover episode page',
            'hoover.org/research (Kotkin / Uncommon Knowledge)',
            'Public episode identification; host/guest, date, title context.'],
           ['World Bank ICP methodology',
            'worldbank.org/en/programs/icp/methodology',
            'PPP concept, price-level equalisation, comparison logic.'],
           ['WDI PPP GDP metadata',
            'databank.worldbank.org — series NY.GDP.MKTP.PP.KD',
            'Definition of PPP GDP in constant 2021 international dollars.'],
           ['WDI nominal GDP',
            'data.worldbank.org/indicator/NY.GDP.MKTP.CD',
            'Official WDI world current-dollar GDP series through 2024 ($111.3T, 2024).'],
           ['WDI population metadata',
            'databank.worldbank.org — series SP.POP.TOTL',
            'Population denominator: de facto midyear estimates.'],
           ['Maddison Project Database 2023',
            'rug.nl/ggdc/historicaldevelopment/maddison',
            'Long-run comparative economic history and benchmark context.'],
           ['IMF WEO April 2026',
            'imf.org/en/publications/weo/issues/2026/04/14',
            'Current macro/projection marker ("Global Economy in the Shadow of War").'],
           ['IMF DataMapper — PPPSH, NGDPD, PPPGDP, LP',
            'imf.org/external/datamapper (@WEO)',
            'Current PPP-share, nominal GDP, PPP GDP, and population markers; world nominal $126.3T, world PPP '
            '$222.8T (2026).'],
           ['UN World Population Prospects 2024',
            'population.un.org/wpp',
            'World population estimates and projections to 2100 (2024, 2050, peak, 2100).'],
           ['QoG Standard dataset',
            'gu.se/en/quality-government/qog-data',
            'Convenient modern country-year file carrying WDI variables.'],
           ['Bairoch (manufacturing)',
            '"International Industrialization Levels from 1750 to 1980"',
            'Manufacturing-output shares during the Great Divergence.']]},
 {'k': 'p',
  't': '<i>Scholarly context used in interpretation includes the Great Divergence debate (Pomeranz; Broadberry et '
       'al.), industrialisation and manufacturing-share histories, the middle-income transition literature, the '
       "Balassa–Samuelson framework, and Frankel's rule on matching ruler to question.</i>"},
 {'k': 'section', 'num': 'Appendix D', 'title': 'Colophon'},
 {'k': 'lede',
  't': '<i>A short account of the instrument, because the essay spends so long insisting the instrument '
       'matters.</i>'},
 {'k': 'p',
  't': '<b>Edition.</b> Eighth edition, June 2026 — the first <i>living</i> edition, built on the seventh-edition '
       'fusion. The seventh edition built on the sixth Claude data-essay edition as its argumentative spine and '
       'ingested the reporting apparatus (denominator section, the full PPP limitations chapter, the source-lane '
       'methodology, the bibliography, and the provenance trail) from the parallel GPT-5.5 Pro publication edition. '
       "It is not a symmetric merge: the spine, prose, and original analysis are the sixth edition's; the audit "
       "layer is imported where it strengthens defensibility, and the GPT draft's scaffolding bloat and redundant "
       'tables were deliberately not carried over. This build additionally adds an up-front global-totals panel '
       '("The World This Essay Divides") and an extended speculative coda — <i>The Long View: Scenarios and '
       'Implications to 2050</i> — developed through three designed-disagreement panels, lifting the figure count '
       'from 16 to 22.'},
 {'k': 'p',
  't': "<b>What the seventh-edition fusion corrected.</b> The sixth edition's world-PPP figure (~$205T) was an "
       'error. Verified directly against IMF WEO April 2026, world PPP GDP for the 2026 projection is <b>$222.8 '
       'trillion</b> in current international dollars (the US is the PPP numeraire, so its PPP GDP equals its '
       "nominal $32.38T; at the IMF's 14.5% US PPP share, the world total is $222.8T). The three PPP lanes — 2026 "
       'current ($222.8T), 2024 current (~$195T), 2024 constant-2021 (~$170T) — are now explicitly distinguished and '
       'never spliced. World nominal ($126.3T), World Bank 2024 nominal ($111.3T), and the IMF country figures all '
       'check out against source.'},
 {'k': 'p',
  't': '<b>What the eighth edition added.</b> This edition is the first to live in a public, version-controlled '
       'repository rather than being rebuilt by hand from chat to chat. Three things were formalised. A '
       'machine-readable consistency suite (fifty-two checks across the identity arithmetic, the source-lane '
       'separations, and every cross-figure relationship) now runs against the data file before any build. A '
       'standing review body — nine experts and fifteen on-call advisors — replaces the ad-hoc panels of earlier '
       'editions. And a four-pass finalisation (logic and mathematics; figures between and within; a literary pass; '
       'an editorial pass) was run against the whole document. That finalisation corrected four figures in the '
       'speculative coda: the cone of outcomes was redrawn so that its 2050 fan is exactly the envelope of the five '
       'scenario bars; each scenario\'s shares were made to sum to one hundred percent with a residual "rest of '
       'world"; Japan\'s price-adjusted line was trimmed so it honours the prose claim that it never crosses about '
       'eight percent; and one deep-history population figure was aligned to its own table. No analytical prose '
       'changed, because the coda speaks in directions, not point forecasts — which is the property that lets the '
       'numbers refresh without the argument moving.'},
 {'k': 'p', 't': '<b>Direction &amp; authorship.</b> Directed and written by Hulki Okan Tabak.'},
 {'k': 'p',
  't': '<b>Models.</b> The sixth-edition spine was composed with Claude (Anthropic); the imported apparatus '
       'originated with GPT-5.5 Pro. This fused edition was assembled and reconciled on Claude Opus 4.8, which '
       'verified the IMF figures against source and ran the panels below.'},
 {'k': 'p',
  't': "<b>Inspiration.</b> A public conversation on the Hoover Institution's <i>Uncommon Knowledge</i> — guest "
       'Stephen Kotkin, host Peter Robinson — at the link the director supplied. This essay is an independent '
       'analysis built from that stimulus; it is not a transcript, an endorsement, or a Hoover publication, and it '
       'attributes no specific figure to the conversation.'},
 {'k': 'p',
  't': '<b>Panel method.</b> Each panel ran as designed disagreement, not theatre, and the chair does not vote. For '
       'the essay core: a deep-thinkers roundtable (logical integrity, hidden assumptions) and an editorial-pass '
       'under the fifteen criteria (consistency, logic, typography, front/back matter, '
       'no-decimal-exceeds-its-source). For the speculative coda, <i>The Long View</i>: three panels at five rounds '
       'each — <b>deep-thinkers</b> (the structural and civilizational analysis, with Ibn Khaldun, Sun Tzu, Rachel '
       'Carson, and Hannah Arendt called in), <b>fx-experts</b> (the monetary-order trajectory, its Turkish-lira '
       'brief adapted to the global reserve-currency question), and a <b>wisepersons</b> panel (the epistemic and '
       'ethical frame — Haraway, Morrison, and Kahle, adapted from their native AI-Skills-governance domain to '
       'supply standpoint, the African absence, the human-stakes reading, and the resilience-versus-efficiency '
       'axis). The author ratifies; the panels argue; the surviving synthesis is incorporated; the dialogue is not '
       'printed.'},
 {'k': 'p',
  't': '<b>Build.</b> One source of truth. The same numbers and prose render three ways — an interactive Chart.js '
       'page, a typeset PDF, and a screen-reader edition — with every figure drawn from the data file, never '
       'hand-placed. Change a number once and all editions follow. From the eighth edition onward this pipeline '
       'lives in a public repository and rebuilds itself when the source data updates; the mechanism is described in '
       'Appendix F.'},
 {'k': 'p',
  't': '<b>Typography.</b> Fraunces for display and italics, IBM Plex Sans for text, IBM Plex Mono for labels. '
       'Oxblood (#993C1D) on warm paper.'},
 {'k': 'p',
  't': '<b>Discipline.</b> PPP carries ±5–10% structural uncertainty; deep-history figures are reconstructions with '
       'wide error bars. Read the ruler first, the direction second, and the decimal point last.'},
 {'k': 'section', 'num': 'Appendix E', 'title': 'The Project in Numbers'},
 {'k': 'lede', 't': '<i>What went into this edition. Recorded because a thinking aid should be auditable.</i>'},
 {'k': 'table',
  'headers': ['Detail', 'Value'],
  'rows': [['Originating prompt',
            "A 2026 Stephen Kotkin conversation on Hoover's <i>Uncommon Knowledge</i> (host Peter Robinson). The "
            'brief: test its memorable GDP-share claims against the data, ruler by ruler, rather than repeat or '
            'debunk them wholesale.'],
           ["This edition's brief",
            'Fuse the two parallel "final" editions into one authoritative document: keep the Claude spine, ingest '
            'the GPT reporting apparatus, correct the IMF world-PPP figure against source, maintain source-lane '
            'discipline, run editorial and logical panels. Then extend: surface the global totals up front, and add '
            'a comprehensive speculative coda (<i>The Long View</i>) developed via three panels at five rounds each, '
            'with six new figures.'],
           ['Source verification',
            'World nominal, world PPP, and seven major-economy nominal/PPP figures re-checked against IMF WEO April '
            '2026 and World Bank WDI 2024. One material correction made (world PPP: $205T → $222.8T).'],
           ['Panels run',
            'Essay core: deep-thinkers (logical integrity) · editorial-pass (15 criteria) · author ratification. '
            'Speculative coda: deep-thinkers · fx-experts · wisepersons, five rounds each. Designed disagreement '
            'throughout; the chair synthesises but does not vote.'],
           ['Figures',
            '22 chart placements plus three reference tables (B1–B3), each rendered from the single data file in two '
            'forms — interactive (Chart.js) and print (PDF). Figures 17–22 belong to the speculative coda.'],
           ['Source lanes',
            'Maddison (deep history) · World Bank WDI / QoG country-sum (modern era) · IMF WEO April 2026 '
            '(present-day marker) · UN WPP 2024 (population) · Bairoch (manufacturing). Kept separate, never '
            'spliced.'],
           ['Discipline rule',
            'No chart is decoration; each must answer a question, expose a ruler change, or prevent a false '
            'inference. No decimal pretends to be more exact than its source permits.'],
           ['Edition lineage',
            'Editions one through seven were static documents, rebuilt by hand across separate chats. The eighth is '
            'the <b>first living edition</b>: the same single source of truth now lives in a public, '
            'version-controlled repository that rebuilds itself when the source data updates.'],
           ['Eighth-edition brief',
            'Migrate the project to a code-first living architecture; formalise the review body; run a four-pass '
            'finalisation (logic and mathematics, figures, literary, editorial); ship the first living edition and '
            'the repository behind it.'],
           ['Consistency suite',
            'Fifty-two automated checks across the identity arithmetic, the three PPP-lane separations, and every '
            'cross-figure relationship — run against the data file before each build. This cycle: ten catches found '
            'and cleared (among them a cone-versus-bars mismatch, scenario shares that did not sum to one hundred '
            'percent, a Japan price-adjusted line that crossed its stated ceiling, and a deep-history population '
            'figure out of step with its table); zero remaining.'],
           ['Review body',
            'Nine standing experts (two economists, an economic anthropologist, two technologists, an '
            'institutions-and-culture specialist, two historians, and a demographer-geopolitical synthesist) plus '
            'fifteen on-call advisors. Designed disagreement; the chair synthesises but does not vote; the author '
            'ratifies.'],
           ['Architecture',
            'Dual. A chat advisor plans and ratifies; a code executor builds and commits. One data file of numbers, '
            'one prose manuscript, three rendered editions (interactive, print, screen-reader). The rendered '
            'editions are never hand-edited.'],
           ['Living cadence',
            'The data file updates on each new IMF / World Bank / UN release, or annually; the checks re-run and all '
            'three editions rebuild from the corrected source. A change of <i>direction</i>, not just decimals, '
            'triggers a new analytical edition through the review body. See Appendix F.'],
           ['Build size',
            'About 3,600 lines of Python across the pipeline; manuscript ~15,400 words; 22 figures plus three '
            "reference tables; this edition's print PDF runs 59 pages."],
           ['Cross-model effort',
            'Produced across nine conversations and five models — five Claude sessions and four other-LLM lines '
            '(GPT-5.5 Pro, Gemini, Grok, DeepSeek), from 31 May 2026. The Claude spine and prose are canonical; the '
            'GPT line supplied the ingested apparatus; the others evaluated. The full provenance-labelled accounting '
            '(measured vs self-reported vs estimated) is kept with the project rather than claimed here as exact.'],
           ['Architecture &amp; governance',
            'Three layers: fixed dated editions for readers, a living openly-licensed public repository as the '
            'source of truth, and a codified skill that is the interface to it. Maintained on a benevolent-dictator '
            'model — the author gatekeeps the canonical release; anyone may fork, correct, or extend. Updating is '
            'optional and promised to no one; a dated snapshot is a complete edition.'],
           ['Publication layer',
            'A fixed Google Books edition (a dated snapshot), distribution through Substack and Medium (each '
            'carrying a banner pointing to the living version), and a reader-facing website hub built around the '
            'interactive edition. The book stays literary; the website is navigational and updatable.']]},
 {'k': 'section', 'num': 'Appendix F', 'title': 'This Is a Living Document'},
 {'k': 'lede',
  't': '<i>Why the eighth edition has a version number and a repository, and what keeps it honest as the numbers '
       'move.</i>'},
 {'k': 'p',
  't': 'Every edition before this one was a static object: a manuscript and a build pipeline that a person carried, '
       'by hand, from one conversation to the next, rebuilding the figures each time a number changed. That worked, '
       "but it made the essay mortal — dependent on a single chat's memory, and out of date the moment the IMF or "
       'the World Bank published a revision. The eighth edition is built differently. Its single source of truth — '
       'one data file of numbers, one prose manuscript, and the renderers that turn them into the three editions you '
       'can read — now lives in a public, version-controlled repository. The document you are holding is a '
       '<i>snapshot</i> of that repository at a fixed version; the repository itself is designed to update.'},
 {'k': 'p',
  't': 'The update is deliberately narrow, and that narrowness is the whole trick. The argument of this essay is not '
       'a forecast. It is a method — separate the rulers, divide out population, watch productivity — and a set of '
       '<i>directions</i>: who is rising, who is plateauing, which gap is closing. Methods and directions do not '
       'expire when a denominator is revised from $205 trillion to $222.8 trillion; only the decimals do. So the '
       "living mechanism touches only the data file. When the IMF's October <i>World Economic Outlook</i> lands, or "
       'the World Bank refreshes its indicators, or the UN issues a new population revision, the numbers are updated '
       'in one place, the consistency suite re-runs its fifty-two checks, and all three editions rebuild from the '
       'corrected source. The prose is not rewritten. If a number moves far enough that a <i>direction</i> changes — '
       'if a plateau becomes a decline, or a laggard begins to converge — that is no longer a data refresh but a new '
       'analytical edition, and it goes back through the review body before it ships.'},
 {'k': 'p',
  't': '<b>The architecture is dual.</b> Two instances of the assistant do different jobs, and keeping them separate '
       'is what keeps the document disciplined. A <i>chat advisor</i> plans, reads the figures as a critic would, '
       "ratifies changes against the project's standing rules, and prepares the exact instructions for a change — "
       'but never edits the manuscript or the data directly. A <i>code executor</i> receives those instructions, '
       'makes the single change, re-runs the checks, rebuilds, and commits the result to the repository with a '
       "message that records what moved and why. The advisor thinks; the executor builds; neither does the other's "
       "job. This is the same division of labour that produced the essay's earlier editions, now written down as the "
       'operating rule of the living document.'},
 {'k': 'p',
  't': '<b>The analysis has a standing review body.</b> Earlier editions convened panels ad hoc — a roundtable here, '
       'an editorial pass there. The eighth edition formalises them into nine resident experts, each holding one '
       'lens the others do not: two economists, one on growth and convergence and one on measurement and the rulers; '
       'an economic anthropologist who keeps the lived body in view behind the aggregates; two technologists, one on '
       'the diffusion of the frontier and one on its physical substrate of compute and power; a specialist in '
       'institutions and legitimacy; two historians, one of the long divergence and one of the postwar order; and a '
       'demographer who also holds the geopolitical fan, the most certain variable and the least certain in one '
       'seat. Fifteen on-call advisors are summoned for the narrower questions a given edition raises, from '
       'semiconductors and energy transition to sovereign debt, migration, trade routes, and data quality. They '
       "argue by design; the chair synthesises but does not vote; the author ratifies. The panel's full composition "
       "and triggers live with the project's skills."},
 {'k': 'p',
  't': '<b>The instruments behind the document</b> are themselves recorded, because an essay that spends fifteen '
       'thousand words insisting the instrument matters should disclose its own. The repository carries the '
       'manuscript, the data file, the renderers, the consistency suite, a methodology that explains how each '
       'edition was made, a running log of every error caught and the standing rule it produced, a metrics file that '
       'counts the editions and the checks, and a small set of skills — one that knows how to update the document '
       'and rebuild it, one that convenes the review body, and one that codifies the annual data-refresh ritual and '
       'the source for every number. Together they are the audit trail. The point of all of it is the same as the '
       'point of the essay: a number is a costume, a direction is the body underneath, and the only way to keep the '
       'two from being confused is to show your work — and to keep showing it as the work changes.'},
 {'k': 'p',
  't': '<b>The shape of the project.</b> The living document is one of three layers, and naming them keeps the claim '
       'honest. There is a <i>fixed, dated edition</i> — this one — for readers to quote; a <i>living public '
       'repository</i> that holds the data, the code, the claim registry, and the correction log, and that anyone '
       'may fork or improve; and a <i>skill</i> that codifies the reasoning and is the interface to the repository '
       'rather than a second source of truth. A reader meets the project as a book or a web page; a researcher meets '
       'it as a repository. The "living" claim is deliberately modest: the editions are dated snapshots, the '
       'repository may be updated by the author or by contributors, and it is promised to no one — if it is never '
       'touched again, this dated edition stands on its own. That modesty is the same discipline the essay asks of '
       'its numbers: say what a thing is, date it, and do not claim more currency than you can keep.'}]
