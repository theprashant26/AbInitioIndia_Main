# Structured content migrated from https://abinitioindia.com/ (fetched 2026-10-01).
# Obvious typos are fixed here; every fix is listed in TYPO_FIXES.

TYPO_FIXES = [
    ("SSAI Introduces", "FSSAI Introduces", "Insight title (Tatkal licence article)"),
    ("truely", "truly", "About page kicker"),
    ("Cummulative", "Cumulative", "About page statistics"),
    ("deep routed", "deep-rooted", "Panasonic testimonial"),
    ("Foreign Intuitional Investors", "Foreign Institutional Investors", "Capital Market Services"),
    ("Indian Public Offerings (IPO)", "Initial Public Offerings (IPO)", "Capital Market Services"),
    ("polling of resources", "pooling of resources", "Mergers & Acquisitions"),
    ("commercial nitigrities", "commercial nitty-gritty", "Mergers & Acquisitions"),
    ("there consolidation", "their consolidation", "Mergers & Acquisitions"),
    ("&its necessary", "&amp; it's necessary", "Mergers & Acquisitions"),
    ("slow moment", "slow movement", "India Entry Strategy"),
    ("pit falls", "pitfalls", "Business Advocacy"),
    ("counter productive", "counterproductive", "Business Advocacy"),
    ("Jhonson &amp; Jhonson", "Johnson &amp; Johnson", "Mentor bio (Ajay Purohit)"),
    ("liasoning", "liaisoning", "Team bio (Neeraj Khanna)"),
    ("Shailey has", "Shaily has", "Team bio (Shaily Chauhan)"),
    ("is an Senior Associate", "is a Senior Associate", "Team bio (Atul Upadhayay)"),
    ("having more 5 years", "having more than 5 years", "Team bio (Deepak Shankar)"),
    ("Vipul kumar Gupta", "Vipul Kumar Gupta", "Team name capitalisation"),
    ("mail@abinitio.com", "mail@abinitioindia.com", "Accessibility statement & privacy policy email"),
    ("mail@ainitioindia.com", "mail@abinitioindia.com", "Privacy policy email"),
    ("How does process work?", "How does the process work?", "FAQ question 2"),
]

def fix(s):
    for a, b, _ in TYPO_FIXES:
        s = s.replace(a, b)
    return s

PHONE_DISPLAY = "+011-40393888"
PHONE_TEL = "+911140393888"
EMAIL = "mail@abinitioindia.com"
WHATSAPP = "https://wa.me/918800808022"
SOCIAL = [("https://www.linkedin.com/company/abinitioindia", "LinkedIn", "bi-linkedin"), ("https://twitter.com/abinitioindia", "X (Twitter)", "bi-twitter-x"),
          ("https://www.facebook.com/abinitioindia", "Facebook", "bi-facebook"), ("https://www.instagram.com/abinitioindia/", "Instagram", "bi-instagram")]

# Sister firm's website, linked from the main menu and the footer (opens in a new tab)
LEGAL_SITE = ("Ab Initio Legal", "http://www.abinitiolegal.in/")

# Client logos already in every theme's assets/img
CLIENTS = [("c-bses.jpg", "BSES Rajdhani"), ("c-iifl.jpg", "IIFL"), ("c-panasonic.jpg", "Panasonic"), ("c-radico.jpg", "Radico Khaitan"),
           ("c-cfs.jpg", "Centre for Sight"), ("c-bk.png", "Burger King"), ("c-airworks.png", "Air Works"), ("c-nawadco.jpg", "Nawadco"),
           ("c-gexter.jpg", "Gexter"), ("c-goban.jpg", "Goban"), ("c-icca.jpg", "ICCA")]

# Homepage copy (from the approved homepages)
HOME = {
    "h1": "True partners to your success",
    "kicker": "Business consultants in New Delhi",
    "lead_a": "We commit to the growth of your business. We are not just consultants; we work with you as a part of your business and help you succeed with efficient, effective advice.",
    "lead_b": "We work with you as a part of your business, giving efficient and effective advice that helps you grow.",
    "lead_c": "We commit to the growth of your business, working with you as a part of your team and delivering efficient, effective advice.",
    "svc_h": "Our expertise across diverse practice areas and sectors",
    "svc_p": "Your requirements are manifold, and so is our experience. All the solutions you need, under one roof.",
    "why_h": "More than just business consultants",
    "why_p": "We have advised across industries, segments and sizes. You grow while we look after the rest.",
    "unique_h": "A unique experience, tailored just for you",
    "unique_p": "Your requirements are manifold, and so is our experience in dealing with them. We provide all the solutions under one roof so you can focus on what matters most: your business.",
}
PILLARS = [("Your business", "You've envisioned a dream. It matters that your advisor understands business.", "bi-lightbulb"),
           ("Our experience", "Diversified experience across India covering the entire corporate life of a business.", "bi-award"),
           ("Tailored solutions", "We advise across industries, segments and sizes, with solutions built for you.", "bi-sliders"),
           ("Your growth", "You grow while we look after the rest, and we celebrate your success with you.", "bi-graph-up-arrow")]

# "How we work" – the advisory process from FAQ question 2 (verbatim steps)
PROCESS_INTRO = "Our team at Ab Initio India LLP understands that every situation is unique. However, there are some common steps in every business advisory process that we follow for a systematic approach:"
PROCESS = [
    ("Understand", "Detailed discussion to understand your business advisory needs."),
    ("Review", "Reviewing your existing business plan (draft business plan), the financial position of your business, market research, competitor research, future plans, etc."),
    ("Scope", "Follow-up meetings to discuss details, services fees, timeline, and final deliverables."),
    ("Model", "Further, we have follow-up meetings for a better understanding of the revenue and expense models of your business to make the best suited overall financial model furtherance of discussions and development."),
    ("Draft", "Draft necessary presentations, further research, executive summaries, etc, and any other document as required by the client. Each document prepared will be thoroughly discussed and reviewed regularly."),
    ("Refine", "Prepare a draft outline of the business plan and discuss feedback and incorporate the necessary changes."),
    ("Implement", "Initiating strategy implementation."),
    ("Support", "Coach the client and continue providing ongoing support ranging from minor to major updates."),
    ("Feedback", "Discuss the feedback on the implementation of the business plan."),
]

TESTIMONIALS = {
    "dinesh": ("My experience with Ab Initio has been phenomenal so far. I confidently recommend their high quality, professional work. If you're working with them, I can say for sure that you are in safe hands.", "Dinesh Kumar Gupta", "Legal Head, Radico Khaitan Limited"),
    "neeraj": ("I remain focused on my business while Abinitio team continue to support me on my every query. The kind of comfort which I get while dealing with AB INITIO is praiseworthy.", "Neeraj Khanna", "MD, BackBencher Whisky"),
    "alok": ("We engaged Ab Initio Team for business acquisition advisory and liaising with financiers, solicitors and vendors. I can say that the Ab Initio Team is highly professional, knowledgeable, committed and hard-working. I can gladly recommend them anytime.", "Alok Upadhayay", "Founder - Digital Presence Today"),
    "raghu": ("Understanding India is a bit difficult task. Better to work with the consultant who understands India, its deep-rooted system and its diversified complications. Happy to recommend Ab Initio.", "Raghu Tondon", "General Counsel, Panasonic India"),
    "jayant": ("The research work of the Ab Initio Team is always best. They go deep into the matter and find out a practical solution.", "Mr Jayant Natrajan", "VP, Indiainfoline Securities Limited"),
}

# ---------------------------------------------------------------- About
ABOUT = {
    "kicker": "Strategy that truly matters",
    "intro_h": "How we manage business",
    "intro": "Our business consulting services focus on your most critical challenges and opportunities like business strategy, fund raising, litigation services, corporate finance, mergers &amp; acquisitions and sustainability across all industries and geographies.",
    "what_kicker": "What we do",
    "what_h": "We help organizations implement the change that matters most to them by strategic restructuring and building enduring capabilities.",
    "results_quote": "Our time and cost effective services look after the entire system so that your energies are concentrated on YOUR BUSINESS.",
    "results_h": "We at Ab Initio India bring deep and functional expertise, yet are known for our holistic perspective.",
    "results": [
        "We efficiently capture value across geographical boundaries as well as between the silos of your organization. We have proven a multiplier effect from optimizing the sum of the parts, not just the individual pieces.",
        "Our Business Growth consultants are adept at analyzing your needs to develop targeted and high impact business interventions, and deploying solutions to close the strategy execution gap, producing measurable bottom line results.",
        "We help organizations across the public, private, and social sectors with the sole objective to create the change which truly matters the most to them.",
    ],
    "stats": [("186%", "Cumulative increase in businesses of our clients"), ("8470", "Hours of expert business advises provided"), ("270", "Business benefited from our services over years")],
    "philosophy_kicker": "The difference",
    "philosophy_h": "Our philosophy",
    "philosophy": [
        "As global business advisors, our philosophy lies in working with you to review realistic opportunities for the ultimate growth and success of your business.",
        "By working in a close partnership with you, we ensure your involvement and total commitment towards the implementation of strategies developed to meet the results.",
    ],
    "mission": "Be your preferred consultant in taking decisions on those areas which actually matter a lot to you, by consistently delivering through logics, ideas and solutions.",
    "vision": "Our Vision is to be a leading global business consulting firm, where the success is measured by the value we deliver to our clients.",
    "testimonials": ["dinesh", "neeraj", "alok"],
    "deals_h": "Transactions handled",
    "deals_tags": ["M &amp; A Services", "Buyout", "Fund Raising", "Factory Establishment"],
    "deals": [
        ("Buyout", "Due diligence and Assets Transfer Agreement (ATA) for a fertilizer unit involving complex transfer process with prior permissions and rectification of land records involving deal size of 11Cr approx."),
        ("Business Transfer as a going concern", "Valuations, Negotiations, Strategic transfer of a running bottling plant in Goa having deal size of 5 cr. Smooth transfer of rights to acquirer in the Export oriented unit in Goa industrial area."),
        ("Brands Buyout", "Due diligence, feasibility study followed by assignment of rights, title and interest in Brand portfolio of FMCG Company. The transfer included the transfer of long term lease, labour and brands on a negotiated price of assets. Deal size of 2.5 Cr."),
        ("Acquisition of Brands Portfolio", "Due diligence, negotiations, valuations and assignment of a brands portfolio of a liquor company and its transfer, registrations, compliance at TM registrar level. Deal size 1.5 Cr."),
        ("Joint venture", "Handled setting up of JV with one of the largest MNC including incorporation of Joint venture in the country, compliances of the MCA, registered office, memorandum, articles change as well as drafting, vetting and negotiations of JV agreements."),
        ("Establishment of Factory", "Advised on the setting-up of plant at Aurangabad starting from acquisition of land, permission to build, Capital subsidy scheme of Government and other permissions to run the plant."),
        ("Change of Land usage (CLU)", "Advised on CLU of land usage in Haryana for setting up of factory, its compliances and permissions within time frame available."),
        ("Business Transfer Agreement (BTA)", "Negotiations, Due diligence with a Japanese company for transfer of business under BTA while the business continues to operate at its strength."),
        ("Government Scheme Benefits", "Advised to organisations for availment of government schemes for long term benefits in VAT, Excise, Sales tax and other subsidies. Deal size 4 Cr."),
        ("Post-acquisition compliances", "Advised on achieving of post-acquisition conditions in the share purchase agreement having multiple level disputes civil and criminal. Deal Size 6.5 Cr."),
        ("Management Disputes", "Advised to promoter of a family owned listed company on dispute between management. The infighting was settled at NCLT followed by sale of land to buyers."),
        ("Funds Raising", "Direct dealing with lenders to fulfil their pre and post funding compliances. Advised on complex documents, drafting, vetting and disbursal. Deal Size 100 cr in multiple tranches."),
        ("Qualified Institutional Placement (QIP)", "Successfully advised on preparation of Placement documents post due diligence, raising of funds at appropriate level. Advised on stock market, SEBI and other corporate compliances. Deal Size 375 Cr."),
        ("Foreign Office", "Advised on setting up for overseas operations, buying of running plants, due diligence, valuation and local laws advisory."),
        ("Assets Reconstruction and Securitisation", "Making of a portfolio, setting up of trust under Securitisation Act, valuation of portfolio, issuance of Pass Through Certificates and selling/reselling of portfolio to multiple investors. Deal Size 18 Cr."),
    ],
}

# ---------------------------------------------------------------- Team
TEAM_INTRO = ("True partners to your success", "Our team is comprised of genuinely gifted minds. Our expertise across diverse practice areas and sectors covers varied and nuanced needs.")
TEAM = [
    ("amit-manchanda", "Mr. Amit Manchanda", "Founder &amp; Managing Partner", None, [
        "Amit Manchanda is specialised hand in Corporate Advisory and Business Consulting. He has worked with top most corporates of the country before starting his dream venture.",
        "Mr. Amit Manchanda is a law graduate &amp; fellow member of ICSI.",
        "He carries more than 20 years of corporate experience in handling a variety of assignments in Arbitration, Corporate &amp; Legal Compliances, Trade Marks Infringements &amp; Protections, Joint Ventures documentation, Takeover of Financial Assets, etc."]),
    ("ateev-kapoor", "Mr. Ateev Kapoor", "Partner", None, [
        "Ateev is a partner at Ab Initio and has more than 15 years in the field of Strategic Assignments, Corporate Affairs, Business Advocacy, Client Relationship Management, and Business Development, Legal Advisory.",
        "Ateev Kapoor is MBA from Cardiff University, UK with more than 15 years of PQE in the field of Strategic Assignments, Corporate Affairs, Business Advocacy, Client Relationship Management and Business Development, Legal Advisory. He has worked with esteemed organizations in the field of Assets Reconstruction, Real Estate, Consulting &amp; Finance."]),
    ("shaily-chauhan", "Shaily Chauhan", "Associate Partner", None, [
        "Shaily Chauhan is an Associate Partner at Ab Initio. Shaily has more than 4 Years of experience in handling a variety of secretarial and compliance functions. She is well versed with NSE &amp; BSE Compliances. She also has the experience of drafting petitions, legal notices, agreements, trademark applications."]),
    ("neeraj-khanna", "Neeraj Khanna", "Associate Partner", None, [
        "Neeraj Khanna is an Associate Partner with Ab Initio. He carries with three years of experience in Secretarial Audits, Corporate Governance Audits, Due Diligence functions and compliances of RBI Laws pertaining to Non-Banking Financial Companies. He also handles liaisoning functions with various statutory and regulatory authorities."]),
    ("vipul-kumar-gupta", "Vipul Kumar Gupta", "Associate Partner", "Senior Life Sciences Regulatory, Policy, Pricing &amp; Corporate Affairs Consultant, Strategic Advisor &amp; Trainer", [
        "Vipul is a senior Life Sciences Regulatory, Policy, Pricing &amp; Corporate Affairs consultant, Strategic advisor and Trainer with 20+ years of experience across the global and Indian healthcare ecosystem."]),
    ("deepak-shankar", "Deepak Shankar", "Sr. Associate", None, [
        "Deepak Shankar is a senior associate at Ab Initio. Deepak has largely practiced in the District and Sessions court and understands the procedural aspects of litigation well.",
        "Deepak Shankar is a Law Graduate from Shimla University having more than 5 years of experience in litigation and contracting. He represents clients on diverse issues in various District Courts, Labour Courts, and Industrial Tribunals."]),
    ("taniya-malhotra", "Taniya Malhotra", "Sr. Associate", None, [
        "Taniya Malhotra is a dynamic and assertive person who graduated in Law from the Faculty of Law, University of Delhi. Advocacy, Solution Strategy client communication and dispute resolution are her forte."]),
    ("atul-upadhayay", "Atul Upadhayay", "Sr. Associate", None, [
        "Atul Upadhayay is a Senior Associate at Ab Initio. He is a law graduate and carries with him 5 years of experience in handling commercial litigation in Delhi &amp; NCR.",
        "His expertise lies in corporate and commercial Litigation including defending criminal prosecutions of organizations and its employees for various non-compliances, defending complaints under Consumer Protection Act etc."]),
    ("divit-arora", "Divit Arora", "Sr. Associate", None, [
        "Divit Arora is a Senior Associate at Ab Initio. He has 5 years of experience in General Corporate and Mergers &amp; Acquisitions, including leading Legal Due Diligences and drafting and negotiating transaction documents.",
        "He also has extensive experience in commercial contracts, including drafting, reviewing and redlining a wide range of agreements across various industries."]),
    ("meher-tandon", "Meher Tandon", "Associate", None, [
        "Meher Tandon has graduated in BBA LLB in the year 2020 and is enrolled with the Bar Council of Delhi. She has an extensive background and knowledge of litigation know-how and the corporate world.",
        "Meher Tandon has mastered the art of drafting and can work her magic with Trust Deeds, Protest Petition, Rejoinder, Written Statement, Indemnity Bonds, Legal Notices, Contracts, Memorandum of Understanding, Articles of Association, Employment contracts, lease deeds, and various other Agreements."]),
    ("simran-singh", "Simran Singh", "Associate", None, [
        "Simran Singh, alumnus Symbiosis Law School, Noida - B.B.A LL.B, has worked closely with the corporate team of various law firms and in-house counsels.",
        "A recurring legal intern with experience of over ten internships and holder of various certified courses in pursuance of her ardent interests, she has an indomitable quest for learning the nuances of contract drafting and mergers and acquisitions."]),
    ("akanksha-pathak", "Akanksha Pathak", "Associate", None, [
        "Akanksha Pathak is an associate at Abinitio India. She has a working experience of 3 years in the field of formation, compliance &amp; regulatory aspects of a corporate entity. (CS, MBA, M.COM &amp; B.COM)"]),
]

MENTORS_INTRO = ("Our guiding light", "Our Mentors, who are experts in delivering supreme corporate services utterly justifies our name, Ab Initio INDIA.")
MENTORS = [
    ("jatinder-chopra", "Jatinder Chopra", [
        "Jatinder Chopra has more than a cumulative 30 years of experience in corporate finance, budgeting, controlling, corporate accounts, taxation &amp; corporate laws in various professional companies. Experience in handling IPO(s) as well as pre–IPO (s) of various companies.",
        "He has spent over 25 years in EPC Companies in Multinational as well as reputed Domestic Companies. Immense work experience in Project Financing, External Commercial Borrowings (ECBs), Working Capital Management &amp; Treasury functions of Group of Companies.",
        "Additionally, he has a stronghold in Vendor appraisal, negotiations, financial vetting all commercial aspects including indirect taxation and payment Terms, etc. Project Monitoring and controlling is the key area and obtained special training from Germany. Extensive experience in handling commercial matters of the Company Experience in handling corporate direct and indirect taxation as well as company law matters and in implementation of SAP and other ERPs."], None),
    ("ur-kapoor", "Mr. U.R. Kapoor", [
        "Mr. U.R. Kapoor earned his Bachelor of Economics from Kirori Mal College, holds his Law degree from Faculty of Law and his post graduate degree from Delhi School of Economics. He has also done Management Services Course from Royal Institute of Public Administration, London, UK.",
        "He is retired as Additional Commissioner of Sales Tax, Government of NCT of Delhi. He has worked with various levels and organs for the government for over 38 years, Private Secretary to the Home Minister of India and Private Secretary to the President of India, New Delhi Municipal Corporation, Education, Health, Power, Co-operative Societies, Sales Tax and State Secretariat etc."], None),
    ("ajay-purohit", "Mr. Ajay Purohit", [
        "Founder member of the team which started up a successful education SBU which consisted of innovative “interactive learning” concept over VSAT communication platform. The concept was taken to market right from the “on table” stage into a proven business model. It is still being run in the market for the last ~20 years."],
        ("In Telecom Passive Infrastructure Business:", [
            "Exposure to writing the Master Services Agreements that are the basis of business / commercial relationships between Infra providers and Telcom companies.",
            "Handled budgeting, forecasting, and target monitoring of nationwide sales.",
            "Formulation of successful business strategies in the dynamic and challenging telecom market and steering of the national team to consistently achieve a top line of &gt;~Rs 500 Cr for several years.",
            "National and international retail channel acquisition and management of 40+ business partner channels. Handled prestigious corporate accounts like HP, Genpact, Hewitt, Wipro, Johnson &amp; Johnson, for corporate training business over VSAT based interactive education system platform.",
            "Managed the retail education channel through a nationwide network of business partners.",
            "Successfully shortlisted deployed VSAT based platform for two-way communication (Video, Audio, and text) between studios and nationwide classrooms using multicasting technology."])),
    ("narender-gupta", "Mr. Narender Gupta", [
        "Mr. Narender Gupta is Graduate in Commerce and Law with Post Graduation in Business Management &amp; Fellow Member of the Institute of Company Secretaries of India.",
        "He has more than 35 years of working experience. His industry exposure is across, Manufacturing, Engineering, Real Estate, Telecom, Broadcasting, Entertainment and Service Sectors. His work exposure includes Legal Matters in Corporate and Litigation environment, Commercial Matters, Issues of Corporate Governance, Public Policy, Regulatory Affairs and Corporate affairs."], None),
    ("ajay-bhargava", "Mr. Ajay Bhargava", [
        "Ajay is a Senior Member of the Dispute Resolution Team at Khaitan &amp; Co, one of the Top law firms in the India. He specializes in Civil, Criminal &amp; Corporate Litigation with over 20 years of experience.",
        "He advises on Constitutional matters, Civil &amp; Criminal matters, IPR laws, Pharmaceutical Sector relates laws, Employment Laws and on corporate – commercial disputes. He also advises on matters before the Investigation Wings relating to corporate criminal investigations and quasi criminal prosecutions (white collar crimes). Ajay is often consulted on M&amp;A transactions to provide tactical and advisory support. He also advises on preventive measures in commercial contracts."], None),
]

# ---------------------------------------------------------------- Services
VALUES = [("Practical", "Practical solutions rather than mere advice"), ("Effective", "Decisions made easy by timely consulting"),
          ("Honest", "Money shall be the last priority"), ("Quality", "Best service standards across industry")]

SERVICES = [
 dict(slug="business-advocacy", title="Business Advocacy", icon="bi-megaphone", blurb="Helping you make the best of trade policies.",
  meta="Abinitio India Provides all details about Business Advocacy. The Firm adopts a unique strategic approach to cater and address your needs and issues.",
  lead=["We assist you with clear demarcated and distinguished communication and interaction platform with the associated bodies of the Government in the most transparent and productive manner.",
        "The Firm adopts a unique strategic approach to cater and address your needs and issues.",
        "Through its large pool of advisors and their inexhaustible experience ideas are adopted and implemented to bring your problems to a conclusive end."],
  quote="raghu",
  body="""<h2>Advocacy Strategy</h2>
<p>Custom-made solutions to help enhance your business via suitable combination of approaches, techniques and messages by which we seek to achieve the advocacy goals and objectives laid out.</p>
<p>Bridging the gap between you and the correct resources having strong professional experience right from across the table.</p>
<p>An amalgamation of methods such as Coalition Building, Networking, Institution Building, Sensitisation, etc. are carried forward in a timeline fashion keeping budgets in mind to yield the most positive outcome.</p>
<h2>Diagnosis of the Issue</h2>
<p>Understanding the issue in detail by estimating the future pit falls and taking into account all aspects of responses being counter productive.</p>
<p>The experts engaged are from the Government sector as well as Legal thereby ensuring the best possible solution with complete astuteness.</p>"""),
 dict(slug="strategic-advisory", title="Strategic Advisory", icon="bi-compass", blurb="A unique strategic approach to cater to and address your needs.",
  meta="At Ab Initio our team of senior consultants provide strategic advisory services from large to mid-sized business. We help our clients with industry knowledge to make decisions.",
  intro_h="Corporate strategies to help our clients navigate successful outcomes.",
  lead=["At Ab Initio we advise our clients with industry knowledge, key issues, and analytic rigor which help them make informed decisions. Our strategies enable businesses to achieve their objectives by capitalizing on opportunities and mitigate all potential risks."],
  quote="raghu",
  body="""<h2>Strategic Advisory</h2>
<p>Organizations might have the most powerful employees &amp; innovative technology but what is essential for the most impactful business value in these times of perpetual state of change with emerging technologies and shift in customer behavior is the right strategic advisory. Strategic Advisory ensures that businesses pull out maximum value from their current systems, avoid potential technology pitfalls and attain the highest return possible.</p>
<p>At Ab Initio our team of senior consultant, provide strategic advisory from large to mid-sized business. We provide executive-level guidance in managing key risk areas, optimizing the value of technology, and introducing innovation to your business in cost-effective measures by constantly reviewing potential risks and opportunities that will improve business operations. We use strategic planning analysis, modeling tools, business valuations, and financial capacity among others to make strategies to support &amp; stimulate your business. We at Ab Initio address the critical stages in the corporate development and business transaction lifecycle, from planning and financial analysis to transaction execution and ongoing monitoring of transaction value. Our strategic advisory services fully understand the financial objectives and long-term goals of our business and make optimal strategies to make a strong execution plan. We first introspect your business at present then we conduct a deep study into the prevailing business environment. We further compare your present strategies with the prevailing market conditions. Then we draft a strategy plan of setting and overall strategic direction. We then further make plans to execute the strategies.</p>
<h2>We provide the following strategic advisory services:</h2>
<ul><li>Capital raising</li><li>Fairness opinions</li><li>Corporate governance</li><li>Strategic alternatives advisory</li><li>Corporate development advisory</li><li>Special committee financial advisory</li><li>Prioritization of shareholder objectives</li><li>Acquisitions, joint ventures, and alliances</li><li>Sale and divestiture planning and advisory</li></ul>"""),
 dict(slug="transaction-advisory", title="Transaction Advisory", icon="bi-arrow-left-right", blurb="Best practices for the Indian financial system.",
  meta="Ab Initio provides Transaction Advisory Services. Our dedicated team helps to provide strategic and financial advice for business.",
  lead=["We at Ab Initio help our client from decision support at origination to deal closing and beyond, i.e., at every step of the transaction. We combine market data with fundamental financial competencies, to support your critical decision-making. We assist our clients by providing them with the information they need to make informed business decisions for buy- and sell-side transaction engagements, refinancings, and other transactions."],
  quote="dinesh",
  body="""<h2>Transaction Advisory</h2>
<p>We at Ab Initio understand that every business involves hard work and sweat. Every business has to overcome challenges on a day-to-day basis in order to achieve its objectives. To avoid any uncertainties in business transactions, transaction advisory plays an important role.</p>
<p>Our dedicated team at Ab Initio helps businesses by providing assistance to reduce any risk. We help our clients from the start to the end and thus act as your business’s support system, and meet requirements for expansion. Our dedicated team possesses the skills and knowledge to provide strategic and financial advice while finalizing any deal. We do our homework by doing proper market research to identify any risk and to identify the next best opportunity. So that the businesses we are assisting can make informed strategic decisions with confidence. We assist our clients at all steps. From deal negotiations to capturing synergies during integration, we help clients gain value and deliver it to stakeholders.</p>
<p>Our analytical skills and real-world experience in diverse situations and unique problems will help in appreciating our clients’ overall objectives and understanding how transactions can influence their business’s success. Our team will navigate and assess risk against potential rewards.</p>
<p>The strength of Ab Initio lies in consistent results and our ability to meet and exceed expectations. Whether you have a turnaround, two companies merging, or a company that should be growing faster, we’re here to help you succeed. No matter how challenging or complex your vision is we at Ab Initio can assist you at every step.</p>"""),
 dict(slug="structure-advisory", title="Structure Advisory", icon="bi-diagram-3", blurb="Critical strategies for achieving overall corporate objectives.",
  meta="We help in understanding a complex business structure and simplifying it in the regulated environment by following the laws and practices of the industry.",
  lead=["We help in understanding a complex business structure or designing and simplifying it in the regulated environment by following the laws and practices dealing with the industry."],
  quote="dinesh",
  body="""<h2>Structure Advisory</h2>
<p>Our team has in-depth experience of working in the top most corporates of the country and carry the experience of designing a financial model which is not only time tested but has also been tested on all the legal and regulatory parameters. We understand the structure parameters and precedents to give a solution that gels with the goal of an organization. We have expertise in designing and delivery of business models which have the potential to reap benefits for a long duration.</p>
<p>Our structuring team has dealt with M&amp;A, takeover, business transfer, Joint Ventures for continuing businesses which have implications of stamp laws, taxation, GST, capital gain, valuations, etc. We devise, design, and implement the strategy by giving it a structure that is best suited to the organizational needs.</p>"""),
 dict(slug="mergers-acquisitions", title="Mergers &amp; Acquisitions", icon="bi-intersect", blurb="Simplifying the complex and cumbersome M&amp;A process.",
  meta="Mergers &amp; Acquisitions means combining the strength of two corporates. It has many facets involving collaboration agreements, Joint Ventures and takeovers.",
  lead=["Mergers &amp; Amalgamation is a general term used for combining strength of two corporates. However, in actual it has got many facets involving Joint Ventures, Take overs, collaboration agreements, polling of resources, creating special purpose vehicles with common objectives or a scheme of arrangement. We cover every aspect and simplify the process for you."],
  quote="dinesh",
  body="""<h2>Joint Venture</h2>
<p>A joint venture can be either Joint shareholding in a single company, Joint ownership on a single asset or joint arrangement for a common objective. In all these arrangements there is a requirement of deep understanding of the industry, the policies/procedures involved in initiating /concluding the arrangement as well as commercial nitigrities among two people with vested interests. The lengthy documents sometimes are the need of the venture but at times become too much complicated to understand.</p>
<p>Our expertise lies in simplifying the document and tilting it towards the practical side of the transaction rather than making it complex and cumbersome.</p>
<h2>Take Over</h2>
<p>A takeover seems to be the easiest transaction of buying shareholding in a company either full or in parts may be in one go or through a series of acquisitions. However, this simple transaction gets different path if pertains to a listed company &amp; takeover is hostile (existing managements unwillingness to part with its equity or control). It generally deals with change of control &amp; requires many approvals like SEBI/CCI/Lenders/State government etc.</p>
<p>We advise our clients to acquire the target company with a strategy. Though in smaller transactions the target is itself in search of bigger partners but in many cases the target may have great growth &amp; would not be interested to part with the stake. In such cases the negotiations become very critical &its necessary that the advisors understand the business well and has experience to deal with target without annoying it.</p>
<p>Our team carries experience in strategizing such takeovers by advising our clients not only on the pricing, structure and timelines but on documentations, approvals and processes.</p>
<h2>Collaboration Agreements</h2>
<p>Such agreements are set of documents carry single objective governed by an agreement defining the rights and obligations of parties. Builders, Real estate developers, Infrastructure companies create such collaborations either direct or through special purpose vehicles (SPV) so as to achieve the common objective.</p>
<h2>Mergers</h2>
<p>A merger is transfer of one company’s assets and liabilities (transferor) into the assets and liabilities of acquirer (transferee company) through a court approved scheme while a scheme can be equally devised to de-merge the new company out of an existing company. These schemes of arrangements can be devised in many ways resulting into few companies/businesses or there consolidation.</p>"""),
 dict(slug="india-entry-strategy", title="India Entry Strategy", card_title="India Entry Advisory", icon="bi-geo-alt", blurb="Helping you understand India better than anyone else.",
  meta="Ab Initio helps with business entry strategy in India. Get complete details about our India Entry Strategy services.",
  lead=["India is a different subject altogether. India seems one country but at the core of it lays different states, union territories, division of north &amp; south, urban &amp; rural, elite &amp; poor and highly educated to illiterates.",
        "We advise our clients to first understand India and see it from the eyes of a philosopher and not as a businessman. One might have no hopes but may get high returns while one with exceptional concept may fail miserably. To achieve the success in India, do business the way Indians do, work as if you belong here is the mantra."],
  quote="dinesh",
  body="""<h2>India Entry Strategy</h2>
<p>India is a different subject altogether. India seems one country but at the core of it lays different states, union territories, division of north &amp; south, urban &amp; rural, elite &amp; poor and highly educated to illiterates. On all these differentiations exists the thickly populated areas with people of diversified background of cast, colour, language, religion and ethnicity. Understanding India is not a task of months or years but generations. The moment one starts digging deep to understand India the layers and layers of confusing ideas will emerge which make it more complex.</p>
<p>Same applies equally on doing business in India. It’s a complex web of laws, rules, regulations, amendments after amendments to keep someone happy. At times one will feel that it’s so easy but the moment you start practical implementation one will come across puzzling thoughts, tantrums, slow moment, easy going approach, holidays and what not! To deal with India you need to have a strategy in place with at least three fall back options. You never know what will click so keep them all your best ones without getting emotionally attached to one. You will like a place, lessor will refuse to let. You will like an employee he will leave you any moment. You like a government policy, tomorrow it’s gone.</p>
<p>Having said this India is abundant team of highly intelligent, loyal and emotional people provided you learn the art of using them too soon. Here businesses are built with a human touch. You will get people who will work for you their entire life with no expectations. You will find landlord offering you drinks when you pay them rent. You will have plenty of opportunities at your disposal provided you apparently show your belongingness to this place. There is history of thousands years of people who came here to won and fallen in love with her.</p>
<p>You should never make the mistake of considering her market of cheap labour or consumption economy. We advise our clients to first understand India and see it from the eyes of a philosopher and not as a businessman. One might have no hopes but may get high returns while one with exceptional concept may fail miserably. To achieve the success in India, do business the way Indians do, work as if you belong here is the mantra.</p>
<h2>We Assist You in Following Ways:</h2>
<ul><li>We help clients to understand India</li><li>We help to build connects between people and capital</li><li>We assist in interpreting policies through the horse’s mouth</li><li>We ensure that investments are based on sound judgements</li><li>We assist in understanding the market, consumer patterns and demand</li><li>We make sure that every penny of client’s expenditure has a sound logic</li></ul>"""),
 dict(slug="regulatory-practice-advisory", title="Regulatory Practice Advisory", icon="bi-shield-check", blurb="Expert opinions on provisions, procedures and practices.",
  meta="Ab Initio offers Regulatory Practice Advisory services in India, including specialist advice on diverse issues across heavily regulated sectors.",
  lead=["We advise on both contentious and non-contentious issues, to some of the largest businesses in India operating in diverse regulated sectors such as Liquor, Broadcasting, Telecom, Agriculture, Pharmaceuticals, Healthcare, Agro-Chemicals, Biotechnology, Food, Aviation, Defence, Real Estate and Infrastructure etc."],
  quote="raghu",
  body="""<h2>Regulatory Practice Advisory</h2>
<p>We provide advisory services including specialist advice on diverse issues such as government-mandated Price Controls, Competition Law and Policy, Grant of Permission issues, License conditions, FDI and FIPB related issues, Tariff issues in Broadcasting and Telecom sectors, Interconnection and Interoperability issues, Platform Access and Denial issues, Quality of Service norms mandated by regulators, Environmental law and Policy issues, Biodiversity law in Life Sciences and Agriculture sectors, etc.</p>
<p>Our focus is driven by unprecedented policy and regulatory issues confronting these heavily regulated industries. New Legislation, Government policies, and regulations in the Indian economy have increased business-planning risks across almost every regulated sector. The dynamic conditions of private-sector commerce and Government oversight of private enterprise are a real threat to both Domestic and Multinational organizations operating in India. In this high-stakes landscape, we aim to provide its clients a coordinated approach to respond to the shifting regulatory and legislative environment.</p>
<p>From analytical planning and risk management, through communications strategy, to administrative and judicial intervention, we work with our Clients every step of the way in navigating the critical intersection of business, law, regulation, policy, and politics.</p>
<p>With our deep experience in a variety of regulated industries, we provide a balanced perspective on key issues. Our strength lies in understanding the issues faced by corporate decision makers because our team members themselves have held key Government &amp; Legal Affairs and In-House positions. We understand how geopolitical issues affect business operations as our Team has worked in complex business and regulatory environments. Our diverse experiences give us an in-depth understanding of what matters most to our clients and allow us to anticipate and advise them on the latest regulatory changes, market developments, legislative actions, and commercial and technical issues.</p>"""),
 dict(slug="capital-market-services", title="Capital Market Services", icon="bi-graph-up-arrow", blurb="Helping you with your on-time capital needs.",
  meta="Ab Initio is a trusted and expert capital markets services provider for the Indian market. Get complete information about capital market rules, policies and procedures.",
  lead=["Now navigate complexity with ‘Ab Initio’ as a trusted and expert capital markets services partner at your side.",
        "As capital markets evolve across the globe, you need a bespoke approach from a service provider with a genuine understanding of how markets are changing.",
        "We can help you unleash your potential with our unrivalled experience and true global reach. Our network of experts can service large transactions across multiple jurisdictions."],
  quote="dinesh",
  body="""<h2>Capital Market Services</h2>
<p>Indian capital market is essentially governed by acts, rules, regulations, policies and procedures promulgated by Securities &amp; Exchange Board of India or SEBI and Reserve Bank of India (RBI). Both SEBI and RBI play a vital role in setting the macro environment &amp; limits within which one can play to raise FDI (Foreign Direct Investments) or Funds from FII’s (Foreign Intuitional Investors), Banks, General public etc. For getting funds from above said resources there is a need of using or floating an instrument depending upon the size, terms, time horizon, industry etc. These instruments can be Commercial papers (CP’s), Non-convertible debentures (NCD’s), Indian Public Offerings (IPO), Foreign Currency Bonds, Global Depository Receipts (GDR), Qualified institutional Placements (QIPs), Equity or preference shares etc.</p>
<p>All these instruments are governed by a set of rules prepared by above said regulators. With passage of time in most of the cases the rules are well settled and procedures well established requiring the following of a prepared check list. Change in rules if any can be tackled at relevant times by in-depth study whenever needed.</p>
<p>There can be cases of ongoing activities like ESOP, Buy Back, Follow on offers, Right issues, Bonus issues, Auction Sales, Takeover (hostile or with consent), delisting, relisting etc.</p>
<p>In all the cases the role of merchant banker, registrar of share transfer, NSDL, CDSL, legal advisor is crucial to achieve the desired objective.</p>
<h2>We Assist You in Following Ways:</h2>
<ul><li>Approval of market regulators</li><li>Funds Flow and Utilisation advisory</li><li>Providing check lists for a corporate action</li><li>Preparing relevant memorandums and reports</li><li>Vetting and drafting of Agreements, Escrow arrangements</li><li>Listing, De-listing, and Relisting of equity and debt instruments</li></ul>"""),
]
for s in SERVICES:
    s["lead"] = [fix(x) for x in s["lead"]]
    s["body"] = fix(s["body"])
    s.setdefault("card_title", s["title"])

# ---------------------------------------------------------------- Contact
CONTACT = {
    "h": "Get in touch",
    "lead": "Business advisory in Compliances, Legal, Regulatory, Corporate Laws, Funding &amp; Investment is our Forte. We provide solutions which are time tested. We believe in solutions rather than stretching the issues. We are your advisor, friend and partner to your success.",
    "intro": "Contact our office to help us fully understand the nature of your business and provide you with the solutions which meet your business requirements.",
    "phones": [("Landline", "+011-40393888", "+911140393888"), ("Contact", "+91 8800 808 022", "+918800808022"), ("Contact", "+91 8800 808 033", "+918800808033")],
    "hours": ("9:00 AM to 6:00 PM", "Monday to Saturday"),
    "offices": [("New Delhi", "1011B, 10th Floor, Indraprakash Building,<br>21 Barakhamba Road, New Delhi – 110001"),
                ("New Delhi", "C 208, LGF, Defence Colony,<br>New Delhi – 110024"),
                ("Gurugram", "Unit No. 1003, 10th Floor, Tower-D,<br>Vatika Light House at Vatika Town Square,<br>Sector 82-A, Gurgaon – 122004, Haryana")],
    "map": "https://www.google.com/maps?q=Indraprakash+Building,+21+Barakhamba+Road,+New+Delhi+110001&output=embed",
}

# ---------------------------------------------------------------- FAQ (answers are HTML; {R} = relative root)
FAQ = [
 ("1. What does Ab Initio India LLP do?", """<p>Being a Global Business Consultant, the services of Ab Initio India LLP focus on your most critical challenges and opportunities like Business Strategy, Fund Raising, Litigation Services, Corporate Finance, Mergers &amp; Acquisitions, and Sustainability across all industries and geographies. Read more about <a href="{R}services.html">our services as business advisors</a> here.</p>"""),
 ("2. How does the process work?", """<p>Our team at Ab Initio India LLP understands that every situation is unique. However, there are some common steps in every business advisory process that we follow for a systematic approach:</p>
<ol><li>Detailed discussion to understand your business advisory needs.</li><li>Reviewing your existing business plan (draft business plan), the financial position of your business, market research, competitor research, future plans, etc.</li><li>Follow-up meetings to discuss details, services fees, timeline, and final deliverables.</li><li>Further, we have follow-up meetings for a better understanding of the revenue and expense models of your business to make the best suited overall financial model furtherance of discussions and development.</li><li>Draft necessary presentations, further research, executive summaries, etc, and any other document as required by the client. Each document prepared will be thoroughly discussed and reviewed regularly.</li><li>Prepare a draft outline of the business plan and discuss feedback and incorporate the necessary changes.</li><li>Initiating strategy implementation.</li><li>Coach the client and continue providing ongoing support ranging from minor to major updates.</li><li>Discuss the feedback on the implementation of the business plan.</li></ol>"""),
 ("3. What services does Ab Initio India LLP provide in “Setting up business in India”?", """<p>Setting up business in India involves the following steps:</p>
<ol><li>Understanding the client’s interest to start up a business in India.</li><li>Setting up detailed meetings for briefing about the potential business ideas around the interest of the client.</li><li>Discussing suitable business entry for client’s idea (Proprietorship, Partnership, LLP, Pvt. Ltd., OPC, PUB LTD, etc.)</li><li>Formulating a suitable execution plan.</li><li>Incorporation of business.</li><li>Applying and obtaining industry-specific licenses and registrations.</li><li>Applying and obtaining revenue law and labor law registrations.</li><li>Opening bank accounts for business.</li><li>Preparing a draft outline of the business plan and discuss feedback and incorporate the necessary changes.</li><li>Initiating strategy implementation.</li><li>Coach the client and continue providing ongoing support ranging from minor to major updates.</li><li>Discuss the feedback on the implementation of the business plan.</li></ol>
<p>At Ab Initio India LLP, our extensive <a href="{R}services/india-entry-strategy.html">India Entry Advisory Services</a> help you in starting your business in India with ease.</p>"""),
 ("4. How do you price your business advisory services and other services?", """<p>In general, there is no pre-determined fixed fee for our business advisory services. The service fee is determined by:</p>
<ol><li>The scope of the project, in terms of the tasks and documents, the client requires help with.</li><li>The quality of the client’s existing materials, including drafts of business plans, financial forecasts, market research, competitive research, etc.</li><li>The vision of the client’s business model, marketing and distribution strategy, financial plans, etc.</li><li>The complexity of the client’s industry and business model.</li><li>The availability of industry information.</li><li>The desired timing relative to Ab Initio India LLP workload. In general, “rush jobs” or “priority jobs” will carry a substantial premium.</li></ol>"""),
 ("5. What happens after Ab Initio India LLP has delivered the final documents?", """<p>The Support Services of Ab Initio India LLP will remain available, at no extra cost to answer follow-up questions, provide business advice, and make minor to major changes to the documents we produced for your business.</p>"""),
 ("6. I have a great product but don’t know how to get it to market. Can Ab Initio India help me with my product launch?", """<p>Ab Initio India LLP can assist with everything from production options, supply chain decisions, packaging decisions, competitor research, marketing strategy, as well as management and operations consulting as well as finances. Please <a href="{R}contact.html">contact us</a> to discuss your situation in confidence.</p>"""),
 ("7. The focus of your business advisory services seems to be on research, planning and strategy. Do you also help clients with implementation?", """<p>Ab Initio India LLP never simply jumps into implementation work without gaining a solid understanding of your particular business and goals. Please <a href="{R}contact.html">contact us</a> to discuss your particular situation and business advisory requirements in confidence.</p>"""),
 ("8. Can you help in providing me with equity investment in my business or provide debt financing?", """<p>Ab Initio India LLP can support your search for funding in many useful ways, including market research, preparation of a business plan, and preparation and review of supporting documents. With our Fund Raising Advisory Services, we can also arrange introductions to qualified funding sources. We also work closely in providing financial services such as business valuations and investor introductions.</p>"""),
 ("9. I am an angel investor. I am considering investing a significant amount of money into a small business. I am worried I am missing something and want someone to evaluate the business itself along with the external market. Can you help me?", """<p>At Ab Initio India LLP our business advisory experts can help you with the research of the external market and perform due diligence on the business itself. We are very good at finding “where the bones are buried.”</p>"""),
 ("10. What industry do you serve or specialize in?", """<p>At Ab Initio India LLP we don’t believe in expertise in any particular but rather an understanding of what investors like to see in a potential opportunity. We take pride in our ability to learn the fundamentals of virtually any industry or technology quickly. Some of the many markets we have served include Renewable Energy, Manufacturing, Internet/E-commerce, Liquor, Telecommunications, Beauty, and Lifestyle.</p>"""),
 ("11. How do I obtain permission to republish an article or an excerpted exhibit?", """<p>Ab Initio allows selected publications to republish our articles on a subject to approval basis. To request permission to republish an article or exhibit, online or in print, please write to <a href="mailto:mail@abinitioindia.com">mail@abinitioindia.com</a> with the following information:</p>
<ul><li>Title and publication date of the article you would like to republish.</li><li>Name and brief background of your organization.</li><li>Where do you intend to post the material.</li><li>Contact name for your permissions manager.</li><li>We ask that our content be used only for educational, informational, or editorial purposes. We do not authorize the use of our content for sales, marketing, business, or promotional purposes.</li></ul>
<p>Please allow two to four weeks for us to review and reply to your request.</p>"""),
 ("12. Does Ab Initio India LLP (www.abinitioindia.com) accept article submissions?", """<p>All the articles on our website are written by our team, we do accept submissions from external thought leaders and practitioners. The bar is the same for all authors:</p>
<p>We look for thinking that is novel, useful, and rigorously substantiated. For external contributors, we also attach weight to work that sheds light on topics that are a priority for our firm and to submissions from recognized leaders in their field.</p>
<p>Please email your work at <a href="mailto:mail@abinitioindia.com">mail@abinitioindia.com</a>.</p>
<p>We review both drafts and proposals. If your submission holds promise, we will be in touch to discuss the content and clarify our editorial process.</p>"""),
]

LEGAL = [  # slug, title, nav label, meta description
    ("privacy-policy", "Privacy Policy", "Privacy policy", "How Ab Initio India LLP collects, uses, discloses, transfers and stores the information of visitors and clients of abinitioindia.com."),
    ("disclaimer", "Disclaimer", "Disclaimer", "The information on the Ab Initio India website is for informational purposes only and is not a substitute for professional legal advice."),
    ("terms-of-use", "Terms of Use", "Terms of use", "The terms and conditions that regulate the use of the Ab Initio India LLP website, www.abinitioindia.com."),
    ("cookie-policy", "Cookie Policy", "Cookie policy", "How Ab Initio India LLP uses cookies and other tracking technologies on abinitioindia.com."),
    ("accessibility-statement", "Accessibility Statement", "Accessibility", "Ab Initio India strives to provide individuals with disabilities equal access to its services, including through an accessible website."),
]

CATEGORY_LABEL = {"Uncategorized": "General"}
