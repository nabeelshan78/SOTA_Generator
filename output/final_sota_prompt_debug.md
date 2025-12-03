
**ROLE:** You are a Principal Academic Reviewer. Your task is to synthesize the provided source documents into a complete "State of the Art" (SOTA) Review Paper.

**CORE DIRECTIVES (STRICT):**
1. **SOURCE OF TRUTH:** - You are provided with text inside `<source_document>` XML blocks. This is your ONLY knowledge base. Do not use external training data.
   - **Scope:** While the Plan suggests specific files for sections, you must scan **ALL** provided source documents to find relevant evidence for every section and citations. Cross-pollinate ideas across files.

2. **CITATION PROTOCOL:** - **Every** substantive claim, data point, or specific idea MUST be cited immediately.
   - **Format:** `(Author, Year)` or `(Author et al., Year)`.
   - **Extraction:** Look for author/year metadata in the document headers or first paragraphs. If explicit metadata is missing, use the filename or `(Source ID: X)`.
   - **Safety:** DO NOT invent authors or years. If a specific claim is crucial but lacks a clear source in the text, mark it as `[citation needed]`.

3. **SYNTHESIS (The Anti-Listicle Rule):** - Do NOT write: "Paper A says X. Paper B says Y."
   - DO write: "While recent studies suggest X (Author, 2023), others argue Y (Author, 2021), indicating a shift in consensus..."
   - Group findings by *concept*, not by *document*.

**THE DOCUMENT ARCHITECTURE:**
You must follow this exact structure (Titles, Headers, and Flow):

### SECTION 1: 1. Introduction
Goals: ["The sacroiliac (SI) joint is a significant source of low back pain, with fusion becoming a viable option when conservative treatments fail <citation author='Rahl et al.' year='2022'>. The increasing number of SIJ fusions highlights the importance of understanding the biomechanical aspects of the procedures.", 'Current knowledge gaps exist regarding the optimal techniques and components used in SI joint fusion, particularly concerning the use of washers with screws. This review aims to address these gaps by analyzing the biomechanical efficacy of washers in SI joint fusion.', 'This review will focus on the biomechanical performance of SI screw fixation, specifically evaluating the impact of using washers across different screw designs in the context of posterior pelvis ring injuries.', 'The review is structured to provide a comprehensive overview of the clinical context, biomechanical principles, device characteristics, and comparative analysis of SI joint fusion techniques, culminating in a synthesis of evidence and identification of unmet needs.']
Mapped Sources: ['Analysis of Complications in Sacroiliac Joint Fusions Using FDA 510(k) Cleared Devices.pdf (Rahl et al., 2022)', 'Berk 2023.pdf (Berk et al., 2023)']

### SECTION 2: 2. Background & Clinical Context
Goals: ["Abstract: SI joint disorders are a well-known medical condition with both surgical and nonsurgical treatment options. Surgical options have involved decortication of the SI joint and permanent fixation using screws and plates during an open surgical procedure <citation author='Cher' year='2015'>. More recently, several devices for minimally invasive SI joint fusion have become commercially available.", "Key Insights: The prevalence of low back pain originating from the SIJ is thought to range anywhere from 2% to 30% <citation author='Rahl et al.' year='2022'>. Cannulated screws are the gold standard for percutaneous treatment of sacroiliac (SI) pelvis ring injuries <citation author='Berk et al.' year='2023'>. The choice of whether to use these screws in combination with a washer is still undecided <citation author='Berk et al.' year='2023'>.", "H3 - Anatomy & Physiology: The SIJs are mobile in all 3 anatomic planes and have been shown to have intra-articular pain generators along with closely associated extra-articular pain generators <citation author='Rahl et al.' year='2022'>. The SI joint is stabilized by strong ligaments and muscles, allowing for limited motion.", "H3 - Pathophysiology: When conservative treatment for SIJ pain fails, arthrodesis becomes a viable option to reduce or eliminate pain from this joint <citation author='Rahl et al.' year='2022'>. Complications can arise from improper implant placement, leading to malposition and potential nerve impingement.", "H3 - Epidemiology: The number of SIJ fusions continues to be on an annually accelerating upward trend <citation author='Rahl et al.' year='2022'>. The complication rate for minimally invasive SIJ arthrodesis has been reported to be between 0% and 18% with revision rates ranging from 0% to 6.3% <citation author='Rahl et al.' year='2022'>."]
Mapped Sources: ['Analysis of Complications in Sacroiliac Joint Fusions Using FDA 510(k) Cleared Devices.pdf (Rahl et al., 2022)', 'Berk 2023.pdf (Berk et al., 2023)', 'Cher 2015.pdf (Cher, 2015)']

### SECTION 3: 3. Clinical Presentation & Diagnosis
Goals: ['Abstract: The clinical presentation of SI joint dysfunction often involves low back pain, which may radiate to the lower extremities. Diagnosis typically involves a combination of physical examination, provocative maneuvers, and imaging studies.', "Key Insights: The most common symptom reported by patients was radicular pain <citation author='Rahl et al.' year='2022'>. Diagnostic criteria include pain provocation tests and imaging to confirm SI joint involvement.", 'H3 - Symptoms & Functional Impact: Core symptoms include low back pain, buttock pain, and pain radiating to the leg. Functional limitations may include difficulty with activities like walking, sitting, and standing.', 'H3 - Diagnostic Criteria & Imaging: Clinical tests and maneuvers are used to assess SI joint pain. Imaging modalities include X-rays, CT scans, and MRI to evaluate the joint and rule out other causes of pain.', "H3 - Current Treatment Landscape: Non-surgical management includes physical therapy, medication, and injections. Surgical indications are considered when conservative treatments fail, with minimally invasive SI joint fusion being a common approach <citation author='Rahl et al.' year='2022'>."]
Mapped Sources: ['Analysis of Complications in Sacroiliac Joint Fusions Using FDA 510(k) Cleared Devices.pdf (Rahl et al., 2022)']

### SECTION 4: 4. CORE DEVICE ANALYSIS: SI JOINT FUSION
Goals: ['Abstract: This section will analyze the iFuse Implant System and the biomechanical impact of washers in SI joint fusion, focusing on screw designs and their performance.', "Key Insights: The iFuse Implant System is a permanent implant used to perform minimally invasive sacroiliac joint fusion <citation author='Cher' year='2015'>. The biomechanical competence of S1-S2 SI screw fixations, with and without using a washer, across three different screw designs was evaluated <citation author='Berk et al.' year='2023'>.", "H3 - iFuse Implant System Overview: The iFuse Implant System is intended for sacroiliac fusion for conditions including sacroiliac joint dysfunction <citation author='Cher' year='2015'>. The iFuse Implant System includes a delivery system to place a series of triangular titanium implants coated with a porous titanium plasma spray across the SI joint using a lateral, transarticular approach under fluoroscopic guidance <citation author='Cher' year='2015'>.", "H3 - Mechanism of Action: The iFuse implant's shape allows for immediate stabilization of the joint and the titanium plasma spray coating allows for biologic fixation in bone <citation author='Cher' year='2015'>. The biomechanical principles involve achieving fusion through stabilization and bone ingrowth.", "H3 - Evidence Summary for Each Device: The survivorship rate with this implant is high and improving <citation author='Cher' year='2015'>. The 4-year survival rate free from revision surgery was 96.46% <citation author='Cher' year='2015'>. The omission of the washer in fully threaded short screws could lead to a significant diminished biomechanical stability <citation author='Berk et al.' year='2023'>."]
Mapped Sources: ['Cher 2015.pdf (Cher, 2015)', 'Berk 2023.pdf (Berk et al., 2023)']

### SECTION 5: 5. COMPARATIVE ANALYSIS
Goals: ['Abstract: This section compares the biomechanical performance of different screw designs (partially threaded, fully threaded short, and fully threaded long transsacral) with and without washers in SI joint fusion.', "Key Insights: Partially threaded short and fully threaded long transsacral screws demonstrated equivalent biomechanical stability under dynamic loading disregarding whether a washer was used or not <citation author='Berk et al.' year='2023'>. Omission of the washer led to a significantly diminished biomechanical stability under dynamic loading with fully threaded short screws <citation author='Berk et al.' year='2023'>.", "H3 - Comparison of Devices: (Rationale, Outcomes, Technical): The clinical rationale for using washers is to enhance fixation and prevent screw intrusion <citation author='Berk et al.' year='2023'>. The study by Berk et al. found that the omission of the washer in fully threaded short screws could lead to a significant diminished biomechanical stability. The study also found that partially threaded short and fully threaded long transsacral screws demonstrated equivalent biomechanical stability under dynamic loading disregarding whether a washer was used or not <citation author='Berk et al.' year='2023'>. Technical differences include screw thread design and length, which influence biomechanical properties.", "H3 - Clinical & Safety Outcomes Comparison: The study by Berk et al. found that the number of cycles to failure and the corresponding load at failure (N) were significantly higher for the fully threaded short screws with a washer versus its counterpart without a washer <citation author='Berk et al.' year='2023'>. The study also found that the omission of the washer led to a significantly diminished biomechanical stability under dynamic loading with fully threaded short screws <citation author='Berk et al.' year='2023'>. The failure modes for all fixation methods were expressed by a fracture of the ilium between the polymethylmethacrylate ilium fixation and the S2 SI screw <citation author='Berk et al.' year='2023'>.", "H3 - Technical Differences + Transition: The study by Berk et al. used three different screw designs: partially threaded short screws, fully threaded short screws, and fully threaded long transsacral screws <citation author='Berk et al.' year='2023'>. The study found that a washer could be optional when using partially threaded short or fully threaded long transsacral S1-S2 screws for treatment of posterior pelvis ring injuries in young trauma patients <citation author='Berk et al.' year='2023'>."]
Mapped Sources: ['Berk 2023.pdf (Berk et al., 2023)']

### SECTION 6: 6. EVIDENCE SYNTHESIS & GAPS
Goals: ['Abstract: This section synthesizes the evidence on the biomechanical efficacy of washers in SI joint fusion, highlighting key findings, limitations, and unmet clinical needs.', "Key Insights: From a biomechanical perspective, a washer could be optional when using partially threaded short or fully threaded long transsacral S1-S2 screws for treatment of posterior pelvis ring injuries in young trauma patients <citation author='Berk et al.' year='2023'>. The omission of the washer in fully threaded short screws could lead to a significant diminished biomechanical stability <citation author='Berk et al.' year='2023'>.", "H3 - Summary of Key Findings: The study by Berk et al. found that the omission of the washer led to a significantly diminished biomechanical stability under dynamic loading with fully threaded short screws <citation author='Berk et al.' year='2023'>. Partially threaded short and fully threaded long transsacral screws demonstrated equivalent biomechanical stability under dynamic loading disregarding whether a washer was used or not <citation author='Berk et al.' year='2023'>.", "H3 - Evidence Gaps & Limitations: The study by Berk et al. used artificial bone models, which may not fully simulate the complexities of human bone <citation author='Berk et al.' year='2023'>. The study's failure modes, fracturing of the ilium, may not be clinically relevant for young patients <citation author='Berk et al.' year='2023'>. Missing torque data on the tightening force of the screws with and without washers is another limitation <citation author='Berk et al.' year='2023'>.", "H3 - Unmet Clinical Needs: Further biomechanical cadaveric studies should be initiated for a reliable interpretation of washerless fixations and their potential for the therapy of the injured posterior pelvis ring <citation author='Berk et al.' year='2023'>. There is a need for more research to determine the optimal screw design and technique for SI joint fusion."]
Mapped Sources: ['Berk 2023.pdf (Berk et al., 2023)']

### SECTION 7: 7. CONCLUSION
Goals: ["The biomechanical study by Berk et al. provides valuable insights into the role of washers in SI joint fusion, suggesting that their use may be optional with certain screw designs <citation author='Berk et al.' year='2023'>.", 'The findings have implications for surgical technique and implant selection, potentially influencing the stability and long-term outcomes of SI joint fusion procedures.', 'Future research should focus on cadaveric studies and clinical trials to validate these findings and further optimize SI joint fusion techniques.', 'The use of washers in SI joint fusion should be carefully considered based on screw design, with the understanding that the omission of washers in fully threaded short screws may compromise biomechanical stability.']
Mapped Sources: ['Berk 2023.pdf (Berk et al., 2023)']


**EXECUTION INSTRUCTIONS:**
1. **Output Format:** Clean Markdown. Start directly with the Title (`# Title`). Use `##` for main sections and `###` for subsections.
2. **Content expansion:** Expand on the "Goals" listed in the plan using detailed evidence from the XML context.
3. **Tone:** High-density, objective, technical, and precise.

--- AVAILABLE SOURCE DOCUMENTS (Context) ---
<source_document id='Analysis of Complications in Sacroiliac Joint Fusions Using FDA 510(k) Cleared Devices.pdf' author='Need to find in source document - Analysis of Complications in Sacroiliac Joint Fusions Using FDA 510(k) Cleared Devices.pdf' year='2022'>
<page number='1'>
Analysis of Complications in Sacroiliac Joint
Fusions Using FDA 510(k) Cleared Devices
Michael D. Rahl, MD, Joseph Weistroffer, MD, and Bruce E. Dall, MD
Study Design: This was a level III—retrospective cohort study.
Objective: The objective of this study was to present an unbiased
report of the current rate of severe complications for Federal Drug
Administration (FDA) 510(k) cleared sacroiliac joint (SIJ) fusions
and investigate the underlying cause of these complications.
Summary of Background Data: The number of yearly SIJ fusions
is on an upward trend. Currently, the most utilized implants to
fuse the SIJ have been FDA 510(k) cleared devices. Studies re-
porting on complications following SIJ fusions are mostly
industry-sponsored.
Materials and Methods: The Manufacturer and User Facility
Device Experience (MAUDE) database was searched for all re-
ported FDA 510(k) cleared SIJ fusion device complications.
Several data points were obtained from each report and re-
corded. The Hospital Inpatient National Statistics and the
Center for Medicare and Medicaid Services (CMS) was also
searched for the number of SIJ fusions performed each year.
Results: A search of the MAUDE database returned 1115 reports,
with the ﬁrst report on June 30, 2011, and the last report on July 28,
2020. Patient injury was the most common type of event reported at
97.5% (1080/1107). Death was reported in 3 patients (0.3%). Mal-
position was the most common device problem at 49.5% (548/
1107). The root cause of these events was primarily user error at
58.2% (644/1107). Revision surgery or reoperation occurred in
92.8% (1028/1107) of reports. Data for SIJ fusions through CMS
showed an overall trend of increasing yearly SIJ fusions.
Conclusions:
The
majority
of
complications
reported
to
MAUDE for FDA 510(k) cleared SIJ fusion devices are user
error due to improper placement of implants. These complica-
tions are likely underreported, and there is currently no formal
tracking system of total SIJ fusions performed to calculate ac-
curate complication and revision rates. Patient injury and health
care costs can potentially be reduced with improved education,
training, and oversight, which is currently lacking.
Key Words: sacroiliac joint, fusion, complications
(Clin Spine Surg 2022;35:E363–E367)
T
he prevalence of low back pain originating from the
sacroiliac joint (SIJ) is thought to range anywhere
from 2% to 30%.1–4 The SIJs are mobile in all 3 anatomic
planes5–8 and have been shown to have intra-articular pain
generators along with closely associated extra-articular
pain generators.9,10 When conservative treatment for SIJ
pain fails, arthrodesis becomes a viable option to reduce or
eliminate pain from this joint.
The number of SIJ fusions continues to be on an
annually accelerating upward trend.11,12 There are many
techniques and hardware options for fusing the SIJ, with
minimally invasive, Federal Drug Administration (FDA)
510(k) cleared implants being the most utilized. The
complication rate for minimally invasive SIJ arthrodesis
has been reported to be between 0% and 18%11–14 with
revision rates ranging from 0% to 6.3%.11,13–17 The ma-
jority of these studies are industry-sponsored and risk
varying degrees of bias.
The purpose of this study was to present an unbiased
report of the current rate of severe complications for FDA
510(k) cleared SIJ fusion implants and to investigate the
reported underlying cause of these complications. Our
hypothesis was that most of the reported complications
are technical errors, which if true, could potentially be
decreased with improved training, education, and over-
sight in coordination with the major spine research and
teaching societies and government institutions.
MATERIALS AND METHODS
The Manufacturer and User Facility Device Expe-
rience (MAUDE) database is a passive surveillance system
that records medical device reports submitted by man-
datory and voluntary reporters of suspected device-
associated deaths, serious injuries, and malfunctions. This
includes complications reported in patients undergoing SIJ
fusions using FDA 510(k) cleared devices. The MAUDE
database was searched in September 2020 using “Sacroil-
iac Joint Fixation” as the Product Class search criteria. A
single reviewer (M.D.R.) manually screened all of the
medical device reports returned from the search. Several
data points, including manufacturer, brand name, date
report was received, event date, event type, device prob-
lem, root cause, initial procedure, number of implants per
side, time to correction, patient symptoms, complication,
corrective action, and outcome, were obtained from each
report and recorded.
Received for publication July 19, 2021; accepted September 15, 2021.
From the Department of Orthopaedic Surgery, Western Michigan Uni-
versity School of Medicine, Kalamazoo, MI.
The authors declare no conﬂict of interest.
Reprints: Michael D. Rahl, MD, Western Michigan University School of
Medicine, 1000 Oakland Drive, Kalamazoo, MI 49008
(e-mail: michael.rahl@med.wmich.edu).
Copyright © 2021 Wolters Kluwer Health, Inc. All rights reserved.
PRIMARY RESEARCH
Clin Spine Surg  Volume 35, Number 3, April 2022
www.clinicalspinesurgery.com | E363
Copyright r 2021 Wolters Kluwer Health, Inc. All rights reserved.

</page>
<page number='2'>
The Hospital Inpatient National Statistics were
searched through the Agency for Healthcare Research and
Quality (AHRQ). Fusion of the SIJ by total discharges
was searched from 2011 to 2017. The number of all fu-
sions, including open, percutaneous, and endoscopic, were
obtained and recorded.
The Center for Medicare and Medicaid Services
(CMS) was also searched through the Medicare Provider
Utilization and Payment Data: Physician and Other Supplier
system. Physician and Other Supplier data from CY2012 to
CY2017 was collected. A search for sacroiliac fusion was
performed, and information related to MD and DO sur-
geons was ﬁltered out. International Classiﬁcation of Disease
(ICD-9 and ICD-10) codes 27280 and 27279 were used.
Total providers and the number of fusions (open and mini-
mally invasive) were obtained and recorded by year.
RESULTS
The MAUDE database was searched from the ﬁrst
report on June 30, 2011, through the last report on July
28, 2020. A total of 1115 reports were identiﬁed. Duplicate
reports and complications not involving the SIJ were re-
moved, leaving 1107 medical device reports. The number
of reports per year steadily increased from 3 in 2009 to 120
in 2014. Reports then increased again in 2017, plateauing
around 150 reports until present (Fig. 1). Surgeon and
patient demographics were not available in these reports.
Eight device manufacturers were included in the
medical device reports (Table 1). Patient injury was the
most common type of event reported at 97.5% (1080/1107).
Death was reported in 3 patients (0.3%). Malposition was
the most common device problem at 49.5% (548/1107). All
common device problems are listed in Table 2. The root
cause of these events was primarily user error at 58.2%
(644/1107). The other root causes are listed in Table 3.
Unilateral SIJ fusion was the initial procedure in 91.3%
(1011/1107) of the medical device reports. Bilateral SIJ fusions,
including
staged
fusions,
made
up
6.6%
(73/1107)
of reports. Three implants per side were used in 911 procedures.
This was followed by 2 implants per side in 101 procedures.
The most common symptom reported by patients
was radicular pain (38%, 421/1107). This was followed by
unspeciﬁed pain (25.7%, 284/1107) and SIJ pain (17.2%,
190/1107). Time to reoperation occurred mostly between 1
week and 11 months (38.9%, 431/1107) (Table 4).
There were 1495 contributing complications reported
in 1107 medical device reports. Complications were most
often the result of an implant breeching the neuroforamen
or sacral cortex with or without nerve impingement (34%,
508/1495). The most common implant involved was the
most cranial implant (61.2%, 311/508). All complications
are listed in Table 5. Revision surgery or reoperation
occurred in 92.8% (1028/1107) of reports.
Ultimate patient outcome was unknown in 58.9%
(653/1107) of reports. Resolved pain, improved pain, and
continued pain were the next most common outcomes at
20.3% (225/1107), 15% (167/1107), and 2.3% (25/1107),
respectively.
0
20
40
60
80
100
120
140
160
180
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
FIGURE 1. Number of adverse sacroiliac joint fusion events reported per year.
TABLE 1. Manufacturer (Brand Name) of Federal Drug
Administration (FDA) 510(k) Cleared Devices Included in
Complication Reports to Manufacturer and User Facility Device
Experience (MAUDE)
Manufacturer (Brand Name)
n (%)
SI-Bone (iFuse)
1047 (94.5)
Zyga (Simmetry)
39 (3.5)
X-Spine Systems (Silex)
10 (0.9)
Warsaw Orthopedics/Medtronic (Rialto)
5 (0.5)
Unknown
2
DePuy Synthes
1
Medacta
1
Spine Frontier (Sacrofuse)
1
Tenon (Catamaran)
1
Total
1107
Rahl et al
Clin Spine Surg  Volume 35, Number 3, April 2022
E364 | www.clinicalspinesurgery.com
Copyright © 2021 Wolters Kluwer Health, Inc. All rights reserved.
Copyright r 2021 Wolters Kluwer Health, Inc. All rights reserved.

</page>
<page number='3'>
Data for SIJ fusions through the Hospital Inpatient
National Statistics (AHRQ) was only available for 2016
and 2017. There were a total of 3220 and 3035 SIJ fusions,
including open, endoscopic, and percutaneous, for 2016
and 2017, respectively. Data on SIJ fusions, including open
and minimally invasive procedures, from the CMS Medi-
care Provider Utilization and Payment Data system was
obtained from 2012 to 2017. The total number of fusions
performed by M.D. and D.O. surgeons for 2012, 2013, and
2014 were 583, 778, and 668, respectively. The total number
of fusions for 2015, 2016, and 2017 were 771, 1082, and
TABLE 2. Device Problem
Device Problem
n (%)
Malposition of device
548 (49.5)
Adverse event without identiﬁed device or use problem
236 (21.3)
Insufﬁcient information
67 (6)
Loss of osseointegration
41 (3.7)
Inadequacy of device shape and/or size
33
Device operates differently than expected
27
Failure to osseointegrate
25
Device slipped
19
Appropriate term/code not available
15
Migration or expulsion of device
13
Improper or incorrect procedure or method
12
Break
11
Unknown
10
Difﬁcult to remove
8
Device dislodged or dislocated
6
Device handling problem
6
Loose or intermittent connection
6
Patient-device incompatibility
4
Contamination
3
Entrapment of device
3
Fitting problem
3
Fracture
3
Equipment failure
2
Unstable
2
Device damaged by another device
1
Extrusion
1
Human device interface problem
1
Unexpected therapeutic results
1
Total
1107
TABLE 3. Root Cause of Complications Determined by
Manufacturer and User Facility Device Experience (MAUDE)
Root Cause
n (%)
User error
644 (58.2)
Unknown
207 (18.7)
Loosening
91 (8.2)
Patient request
37 (3.3)
Procedural
27 (2.4)
Late recurrence of symptoms
18
Pseudoarthrosis
16
Fall
16
Infection
12
Poor patient selection
6
Hematoma
6
Precaution
4
Postoperative infection
4
Patient noncompliance
3
Other pain generators then sacroiliac joint
3
Fracture
3
Surgeon’s decision
2
Equipment failure
2
Allergy
2
Motor vehicle accident
1
Deep venous thrombosis
1
Chronic pain
1
Bleeding
1
Total
1107
TABLE 4. Time to Reoperation Following Complication
Time to Reoperation
n
Intraoperative
35
&lt; 1 wk
105
1 wk–1 mo
431
1–3 y
377
4+ y
69
Unknown
90
Total
1107
TABLE 5. Description of Complication
Complication
n
Superior implant
Into neuroforamen/breeched cortex/impinging on nerve
311
Too short
3
Too proud
8
Malpositioned
10
Loose
28
Middle implant
Into neuroforamen/breeched cortex/impinging on nerve
77
Too short
19
Too proud
10
Malpositioned
8
Loose
23
Inferior implant
Into neuroforamen/breeched cortex/impinging on nerve
47
Too short
29
Too proud
16
Malpositioned
333
Loose
31
Implant not speciﬁed
Into neuroforamen/breeched cortex/impinging on nerve
73
Too short
11
Too proud
15
Malpositioned
43
Loose
105
Neuromusculoskeletal
Pseudoarthrosis/nonunion
33
Fracture
14
Scar tissue with nerve compression
2
Nerve damage
2
Medical
Infection
23
Pulmonary embolism
4
Cardiac
4
Allergy
2
Equipment
Guide pin/tool broken or malpositioned
11
Hematologic
Hematoma
15
Pseudoaneurysm/vascular injury/bleeding
13
Deep venous thrombosis
3
Other
Unknown
107
Patient request
61
Nonsterile implant
1
Total
1495
Clin Spine Surg  Volume 35, Number 3, April 2022
Analysis of Complications in Sacroiliac Joint
Copyright © 2021 Wolters Kluwer Health, Inc. All rights reserved.
www.clinicalspinesurgery.com | E365
Copyright r 2021 Wolters Kluwer Health, Inc. All rights reserved.

</page>
<page number='4'>
1165, respectively. Neither database provided information
on the indication for surgery or the type of device used.
DISCUSSION
The MAUDE database tracks global complications to
include FDA 510(k) cleared SIJ fusion devices marketed in
the United States. There were 1107 complications reported
to MAUDE over an 11-year period that were considered
severe, with most causing patient injury. Of these compli-
cations, 92.8% required reoperation. The current literature
reports an overall low complication rate following minimally
invasive SIJ arthrodesis. This number ranges anywhere from
0% to 18%.11–14 Revision and reoperation rates reported
range anywhere from 0% to 6.3% based on total SIJ
fusions.11,13–17 Complications reported to MAUDE are
conducted as passive surveillance. While the manufacturers
of these devices are required to report all complications, the
number of complications is likely underreported by up to
35%.18 This is because reporting is voluntary for health care
professionals, patients, and consumers. An active surveil-
lance system would offer a more accurate representation of
true complication numbers and reoperation rates.
Exacting an accurate number for the complication
rate when using these FDA 510(k) cleared devices for SIJ
fusions is difﬁcult because there is a complete lack of
formal tracking for the number of SIJ fusions performed.
Currently, there is no database that tracks all SIJ fusions
performed in the United States. CMS does track SIJ fu-
sions under their Provider Utilization and Payment Data
system. From 2012 to 2017, their numbers show SIJ fu-
sions increasing from 582 in 2012 to 1165 in 2017. A study
by Schoell et al12 used the Humana database and found
that from 2007 to 2014, the number of SIJ fusions in-
creased from 14 in 2007 to 142 in 2014. Two SI-Bone
sponsored studies showed that their product was im-
planted 31 times in 2009, and this steadily increased to
3611 in 2012, while the overall number of fusions between
2009 and 2014 was 11,820.11,19 The SI-Bone Web site re-
ports over 45,000 SIJ fusions since 2009 using their
product.20 If ∼80% of SIJ fusions use SI-Bone’s iFuse
system, a conservative estimate, it could be estimated that
∼60,000 SIJ fusions may have been performed over the
time period in question. This would put the complication
rate at about 2%. Due to likely underreporting to the
MAUDE database, the true percentage is most likely
much higher. The AHRQ also has the Hospital Inpatient
National Statistics that report fusion of the SIJ by total
hospital discharges. They reported 3220 discharges in
2016, followed by 3035 discharges in 2017. If these num-
bers were to be hypothetically extrapolated out to include
the 10 years this study covers, the overall number of SIJ
fusions would be far more, making the likely percentage of
complications much higher. The American Spine Registry
does not currently track SIJ fusions, making it impossible
for the major orthopedic, neurosurgery, and spine aca-
demies and societies to follow this data accurately. While
there is similarly no formal tracking of all of the SIJ fu-
sions performed in the United States yearly, it can be seen
that with the available data, the number of SIJ fusions
performed each year continues to increase.
Given that an accurate number of SIJ fusions using
FDA 510(k) cleared devices in the United States each year
cannot be generated, the severe complications that have
been reported are meaningful because they are occurring
with an increasing trend. They are altering patients’ lives
and do result in death, morbidity, and many return trips to
the operating room. Therefore, these MAUDE reports are
worth reviewing by those either directly impacted by them
or in a position to make potential positive changes.
The root cause of the complications reported to
MAUDE was user error at 58.2% (644/1107). The root
cause was further broken down into speciﬁc complica-
tions. Malposition of the implant(s) was the most common
device problem reported at 49.5% (548/1107). This rate is
slightly higher than the symptomatic malposition rate re-
ported by Cher et al19 at 38.4%. Complications were most
often the result of an implant breeching the neuroforamen
or sacral cortex with or without nerve impingement (34%,
508/1495). The most common implant involved was the
most cranial implant (61.2%, 311/508). More than 50% of
the complications reported to MAUDE were due to sur-
geon error. Therefore, a signiﬁcant number of these
complications were potentially avoidable. The available
data currently lacks speciﬁc surgeon demographics, so
further categorization is not possible.
Returning to the operating room for additional
procedures due to complications increases the cost to the
health system. Overall, 92.8% of the complications re-
ported to MAUDE needed to return to the operating
room for an additional procedure. Of these, 9.5% re-
quired reoperation within 1 week, and 38.9% returned to
the operating room between 1 week and 1 year. Childers
and Maggard-Gibbons,21 recently showed that the cost
of an inpatient operating room was $37.45 per minute. If
a separate trip is needed to return to the operating room,
then costs associated with this surgical procedure in-
crease drastically.
Formal education regarding SIJ fusions is currently
lacking, as there is no standard central institution within
spine surgery or the government that provides surgical
education for the dysfunctional SIJ. Currently, the in-
dustry and its surgeon surrogates deliver most of the
training. Informal training from partners and other more
experienced surgeons is also common, with the under-
standing that they too have not been formally trained via a
standard educational protocol that is not proprietary.
With the increasing number of SIJ fusions each year and
with most of the complications reported being surgeon
error, an argument can be made that there needs to be
formal training. Cher et al19 reported that revision rates
dropped as the number of SIJ fusion cases performed in-
creased (6.0% down to 0.7%). In their study, 2.6% of
surgeons were responsible for 34% of revisions. While
more experience leads to fewer complications is a truism
for any surgery, formal training in SIJ fusions during
residency and fellowship is lacking and making this
learning curve steeper. With more education, training, and
Rahl et al
Clin Spine Surg  Volume 35, Number 3, April 2022
E366 | www.clinicalspinesurgery.com
Copyright © 2021 Wolters Kluwer Health, Inc. All rights reserved.
Copyright r 2021 Wolters Kluwer Health, Inc. All rights reserved.

</page>
<page number='5'>
experience, the number of complications and the need for
reoperation should decrease. This lack of education
and training is also reﬂected in the orthopedic and
neurosurgery board examinations. Currently, there is
nothing mentioned regarding the SIJ or SIJ fusion surgery
in the American Board of Neurological Surgery board
preparation Content Categories. The American Board of
Orthopedic Surgery examination preparation Blueprint
mentions that at least 1 question will address sacroiliac
dysfunction but is not necessarily speciﬁc to fusions.
While the numbers of complications reported to
MAUDE are most likely less than the true value, this is
the ﬁrst analysis of all the available data on the 510(k)
cleared devices being utilized for this purpose over a
consecutive 10-year period. An industry-sponsored study
was published in 2015 that looked speciﬁcally at their own
device and MAUDE-reported complications.19 More
studies are needed to further evaluate the underlying
causes and true complication and revision rates following
SIJ fusions. With the implementation of formal training
and more transparent tracking systems, the number of
complications should decrease, making this surgery much
safer for patients.
This study has several limitations. This is a retro-
spective database analysis. While temporal trends, risk-
stratiﬁcation, and cost-analysis are possible, there are few
studies available to validate these database ﬁndings and
their inherent limitations.22 Data obtained for this study
regarding SIJ fusion complications is from a passive sur-
veillance system. Therefore, we believe complications from
this procedure are signiﬁcantly underreported. There is
currently no standardized tracking system of total annual
SIJ fusions performed. Therefore, accurate complication
and reoperation rates are impossible to calculate. The best
available data was obtained, extrapolated, and analyzed for
overall trends. More speciﬁc information regarding surgeon
and patient demographics was not available to further an-
alyze possible contributing factors to these complications.
Finally, user error is a broad term. While more speciﬁc
information was not available, it was determined that the
root cause of these complications was due to the person
placing the implant, not the device itself. SIJ fusions can be
difﬁcult, and the implants are not perfect.
In conclusion, the majority of complications reported
to MAUDE for FDA 510(k) cleared SIJ fusion devices are
from user error due to improper placement of implants.
Many of these reported complications required a return to
the operating room for correction, which did not always
resolve the symptoms resulting from those complications.
The complications reported and examined here are likely
underreported, and there is currently no formal tracking
system of total SIJ fusions performed to calculate accurate
complication and revision rates. Patient injury and health
care costs associated with these fusions can likely be re-
duced with improved education, training, and oversight.
REFERENCES
1. Maigne JY, Aivakiklis A, Pfefer F. Results of sacroiliac joint double
block and value of sacroiliac pain provocation test in 54 patients with
low back pain. Spine (Phila Pa 1976). 1996;21:1889–1892.
2. Manchikanti L, Singh V, Pampati V, et al. Evaluation of the relative
contributions of various structures in chronic low back pain. Pain
Physician. 2001;4:308–316.
3. Sembrano JN, Polly DW Jr. How often is low back pain not coming
from the back? Spine (Phila Pa 1976). 2009;34:E27–E32.
4. Schwarzer AC, Aprill CN, Bogduk N. The sacroiliac joint in chronic
low back pain. Spine (Phila Pa 1976). 1995;20:31–37.
5. Kissling RO, Jacob HA. The mobility of the sacroiliac joint in
healthy subjects. Bull Hosp Jt Dis. 1996;54:158–164.
6. Miller JA, Schultz AB, Andersson GB. Load-displacement behavior
of sacroiliac joints. J Orthop Res. 1987;5:92–101.
7. Sturesson B, Uden A, Vleeming A. A radiostereometric analysis of
movements of the sacroiliac joints during the standing hip flexion
test. Spine. 2000;25:364–368.
8. Vleeming A, van Wingerden JP, Snijders CJ, et al. Mobility in the
sacroiliac joints in the elderly: a kinematic and radiological study.
Clin Biomech. 1992;7:170–176.
9. McGrath C, Nicholson H, Hurst P. The long posterior sacroiliac
ligament: a histological study of morphological relations in the
posterior sacroiliac region. Joint Bone Spine. 2009;76:57–62.
10. Szadek KM, Hoogland PV, Zuurmond WW, et al. Possible
nociceptive structures in the sacroiliac joint cartilage: an immuno-
histochemical study. Clin Anat. 2010;23:192–198.
11. Miller LE, Reckling WC, Block JE. Analysis of postmarket
complaints database for the iFuse SI Joint Fusion System: a
minimally
invasive
treatment
for
degenerative
sacroiilitis
and
sacroiliac joint disruption. Med Devices (Auckl). 2013;6:77–84.
12. Schoell K, Buser Z, Jakoi A, et al. Postoperative complications in
patients undergoing minimally invasive sacroiliac fusion. Spine J.
2016;16:1324–1332.
13. Graham Smith A, Capobianco R, Cher D, et al. Open versus minimally
invasive sacroiliac joint fusion: a multi-center comparison of perioper-
ative measures and clinical outcomes. Ann Surg Innov Res. 2013;7:14.
14. Vanaclocha V, Herrera JM, Saiz-Sapena N, et al. Minimally invasive
sacroiliac joint fusion, radiofrequency denervation, and conservative
management for sacroiliac joint pain: 6-year comparative case series.
Neurosurgery. 2018;82:48–55.
15. Araghi A, Woodruff R, Colle K, et al. Pain and opioid use outcomes
following minimally invasive sacroiliac joint fusion with decortica-
tion and bone grafting: the Evolusion clinical trial. Open Orthop J.
2017;11:1440–1448.
16. Polly DW, Swofford J, Whang PG, et al. Two-year outcomes from a
randomized controlled trial of minimally invasive sacroiliac joint
fusion vs. non-surgical management for sacroiliac joint dysfunction.
J Int Spine Surg. 2016;10:28.
17. Rappoport LH, Luna IY, Joshua G. Minimally invasive sacroiliac
joint fusion using a novel hydroxyapatite-coated screw: preliminary
1-year clinical and radiographic results of a 2-year prospective study.
World Neurosurg. 2017;101:493–497.
18. Heipel D, Ober JF, Edmond MB, et al. Surgical site infection
surveillance for neurosurgical procedures: a comparison of passive
surveillance by surgeons to active surveillance by infection control
professionals. Am J Infect Control. 2007;35:200–202.
19. Cher DJ, Reckling WC, Capobianco RA. Implant survivorship
analysis after minimally invasive sacroiliac joint fusion using the
iFuse Implant System. Med Devices (Auckl). 2015;8:485–492.
20. SI-Bone Inc. Investor relations: overview; 2020. Available at: https://
investor.si-bone.com/. Accessed June 16, 2021.
21. Childers CP, Maggard-Gibbons M. Understanding costs of care in
the operating room. JAMA Surg. 2018;153:e176233.
22. Alluri RK, Leland H, Heckmann N. Surgical research using national
databases. Ann Transl Med. 2016;4:393.
Clin Spine Surg  Volume 35, Number 3, April 2022
Analysis of Complications in Sacroiliac Joint
Copyright © 2021 Wolters Kluwer Health, Inc. All rights reserved.
www.clinicalspinesurgery.com | E367
Copyright r 2021 Wolters Kluwer Health, Inc. All rights reserved.

</page>
</source_document>

<source_document id='Berk 2023.pdf' author='Till Berk, Ivan Zderic, Peter Schwarzenberg, Torsten Pastor, Sascha Halvachizadeh, Geoff Richards, Boyko Gueorguiev and Hans-Christoph Pape' year='2023'>
<page number='1'>
Citation: Berk, T.; Zderic, I.;
Schwarzenberg, P.; Pastor, T.;
Halvachizadeh, S.; Richards, G.;
Gueorguiev, B.; Pape, H.-C. Is a
Washer a Mandatory Component in
Young Trauma Patients with S1-S2
Iliosacral Screw Fixation of Posterior
Pelvis Ring Injuries? A Biomechanical
Study. Medicina 2023, 59, 1379.
https://doi.org/10.3390/
medicina59081379
Academic Editors: Umile
Giuseppe Longo, Vicenzo Denaro
and Edgaras Stankeviˇcius
Received: 1 May 2023
Revised: 21 July 2023
Accepted: 25 July 2023
Published: 28 July 2023
Copyright:
© 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
medicina
Article
Is a Washer a Mandatory Component in Young Trauma Patients
with S1-S2 Iliosacral Screw Fixation of Posterior Pelvis Ring
Injuries? A Biomechanical Study
Till Berk 1,2,3,*
, Ivan Zderic 1
, Peter Schwarzenberg 1, Torsten Pastor 4
, Sascha Halvachizadeh 2,3
,
Geoff Richards 1
, Boyko Gueorguiev 1
and Hans-Christoph Pape 2,3
1
AO Research Institute Davos, Clavadelerstrasse 8, 7270 Davos, Switzerland
2
Department of Trauma, University Hospital Zurich, Raemistrasse 100, 8091 Zurich, Switzerland;
hans-christoph.pape@usz.ch (H.-C.P.)
3
Harald-Tscherne Laboratory for Orthopedic and Trauma Research, University of Zurich, Sternwartstrasse 14,
8091 Zurich, Switzerland
4
Department of Orthopaedic and Trauma Surgery, Cantonal Hospital Lucerne, 6000 Lucerne, Switzerland
*
Correspondence: till.berk@usz.ch
Abstract: Background and purpose: Cannulated screws are standard implants for percutaneous fixa-
tion of posterior pelvis ring injuries. The choice of whether to use these screws in combination with
a washer is still undecided. The aim of this study was to evaluate the biomechanical competence
of S1-S2 sacroiliac (SI) screw fixation with and without using a washer across three different screw
designs. Material and Methods: Twenty-four composite pelvises were used and an SI joint injury type
APC III according to the Young and Burgess classification was simulated. Fixation of the posterior pelvis
ring was performed using either partially threaded short screws, fully threaded short screws, or fully
threaded long transsacral screws. Biomechanical testing was performed under progressively increasing
cyclic loading until failure, with monitoring of the intersegmental and bone-implant movements via
motion tracking. Results: The number of cycles to failure and the corresponding load at failure (N) were
significantly higher for the fully threaded short screws with a washer (3972 ± 600/398.6 ± 30.0) versus
its counterpart without a washer (2993 ± 527/349.7 ± 26.4), p = 0.026. In contrast, these two parameters
did not reveal any significant differences when comparing fixations with and without a washer using
either partially threaded short of fully threaded long transsacral screws, p ≥0.359. Conclusions: From
a biomechanical perspective, a washer could be optional when using partially threaded short or fully
threaded long transsacral S1-S2 screws for treatment of posterior pelvis ring injuries in young trauma
patients. Yet, the omission of the washer in fully threaded short screws could lead to a significant
diminished biomechanical stability.
Keywords: biomechanics; motion tracking; posterior pelvis ring injury; S1-S2 sacroiliac screw ﬁxation;
synthetic pelvic bone model; transsacral ﬁxation; washer; washerless
1. Introduction
Cannulated screws are the gold standard for percutaneous treatment of sacroiliac
(SI) pelvis ring injuries [1,2]. A combined ﬁxation at both S1 and S2 levels via two SI
screws provides the best type of ﬁxation in case of a vertical pelvic instability [3,4]. Most
common, screws of 6.5 mm or 7.3 mm diameter are used together with washers [5], the latter
considered as advantageous regarding biomechanical ﬁxation enhancement [6]. While
there is a common agreement on the surgical treatment, the question of possible implant
removal (IR) remains controversial. Literature provides extensive data on IR rates following
SI screw ﬁxation, amounting up to 57% in follow-up cohort studies [7]. Typical indications
for IR are screw malposition, non-union, screw loosening, as well as iatrogenic damage
to the L5 level or sacral nerve roots [8–11]. A complete IR might be indicated in cases
Medicina 2023, 59, 1379. https://doi.org/10.3390/medicina59081379
https://www.mdpi.com/journal/medicina

</page>
<page number='2'>
Medicina 2023, 59, 1379
2 of 11
with infection, allergic reactions, as well as unsettled pain or following an explicit patient
request. However, complications following IR are common and range between 3 and
20% [12–14]. The fusion of the SI joint, especially in young and active patients, must
be considered unphysiological. It was conversely stated that IR is justiﬁed in younger
patients [7]. Some authors even recommend implant removal routinely [8,15]. Due to the
difﬁculty and proneness to intraoperative problems, the retrieval of the washer can be the
most demanding part of the surgery and constitute the longest part of the surgery [16,17].
Therefore, Oberst et al. suggested an endoscopic IR in order to reduce x-ray exposure and
soft tissue damage [18]. Although young patients with predominantly physiological bone
quality represent a clearly different patient clientele than geriatric patients, hardly any
implants are speciﬁcally designed to patient’s age. Although there are surgical procedures
and techniques that are adapted to the age of the patient, most implants are generic. Hence,
young patients could potentially beneﬁt from standard S1-S2 SI screw treatment excluding
the washer, especially in view of IR, where surgery time, blood loss, surgical exposure,
radiation exposure, and complications could be signiﬁcantly lower. However, to our
knowledge, the surgical method of S1-S2 SI screw ﬁxation of the posterior pelvis ring
without the washer has never been evaluated biomechanically.
Purpose
The aim of this study was to investigate the biomechanical competence of S1-S2 SI
screw ﬁxations, with and without using a washer, across three different screw designs—
(1) partially threaded, (2) fully threaded short, or (3) fully threaded long transsacral SI
screws. The focus was to obtain a holistic picture of construct stability, including the one
immediately after instrumentation, as well as the temporal stability decay during dynamic
loading, together with the ultimate construct endurance. In addition, relative movements
between the two bone segments, between the screw and the ilium, as well as between the
screw tip and the sacrum were assessed. These parameters were speciﬁcally chosen given
the known common clinical failure modes associated with SI screw ﬁxation, namely screw
cutout or loosening, resulting in eventual overall ﬁxation failure [19,20].
2. Materials and Methods
Twenty-four composite pelvises (Model 4060®, Synbone, Zizers, Switzerland) were
used. An SI joint injury type APC III according to the Young and Burgess classiﬁcation was
simulated in all specimens [21]. To induce this injury, the material of the symphysis as well
as the SI joint was removed, resulting in a total instability.
Specimens were stratiﬁed into three sets of two groups each for instrumentation as
follows (Figure 1):
Set 1:
•
Group PT w/: Fixation of the posterior pelvis ring with two 7.3 mm partially threaded
short cannulated self-tapping screws (lengths: 90 mm for S1 and 65 mm for S2) and
washers (diameter 13.0 mm, thickness 6.6 mm).
•
Group PT w/o: Fixation of the posterior pelvis ring with two 7.3 mm partially threaded
short cannulated self-tapping screws (lengths: 90 mm for S1 and 65 mm for S2)
without washers.
Set 2:
•
Group FT w/: Fixation of the posterior pelvis ring with two 7.3 mm fully threaded
short cannulated self-tapping screws (lengths: 90 mm for S1 and 65 mm for S2) and
washers (diameter 13.0 mm, thickness 6.6 mm).
•
Group FT w/o: Fixation of the posterior pelvis ring with two 7.3 mm fully threaded
short cannulated self-tapping screws (lengths: 90 mm for S1 and 65 mm for S2)
without washers.

</page>
<page number='3'>
Medicina 2023, 59, 1379
3 of 11
Set 3:
•
Group TS w/: Fixation of the posterior pelvis ring with two 7.3 mm fully threaded
long transsacral cannulated self-tapping screws (lengths: 175 mm for S1 and 160 mm
for S2) and washers (diameter 13.0 mm, thickness 6.6 mm).
•
Group TS w/o: Fixation of the posterior pelvis ring with two 7.3 mm fully threaded
long transsacral cannulated self-tapping screws (lengths: 175 mm for S1 and 160 mm
for S2) without washers.
 
Figure 1. Inlet (uppercase letters) and outlet (lower case letters) x-rays after instrumentation showing
specimens from groups TS w/(A,a), TS w/o (B,b), FT w/(C,c), FT w/o (D,d), PT w/(E,e) and PT
w/o (F,f).
Equal numbers of three right and three left pelvis sides were utilized in each group
(n = 6). The surgical treatment was performed according to the AO principles [22] as
follows. After reduction of the SI joints, the self-tapping screws were positioned over
a previously placed guidewires perpendicular to the SI joint, entirely within the artiﬁcial
bone, avoiding any perforations. The insertion of the guidewires was performed with
a custom aiming guide, allowing a standardized placement through a single attempt
without any perforations or cortical disturbances. First, the S1 SI screw was positioned,
followed by the S2 SI screw. The screws ranged to the midline of the sacral vertebra in
groups PT w/, PT w/o, FT w/and FT w/o, and to the contralateral ilium cortex in groups
TS w/and TS w/o, and were tightened according to the operator’s best judgment. Post
instrumentation, true lateral, inlet and outlet x-rays were captured to verify the positioning
of the inserted screws (Figure 1).
All screws and washers were made of stainless steel (316LVM) and the same man-
ufacturer (DePuy Synthes, Zuchwil, Switzerland) provided all implants. The anterior
pelvis ring was cut by sawing the pelvic ramus at the middle of the shaft on the ipsilateral
and contralateral sides, as this reﬂects the injury pattern under investigation. A qualiﬁed
surgeon operated all pelvises.
2.1. Biomechanical Testing
The biomechanical testing procedure and equipment was described in a previous
study [23]. The system was equipped with a 5 kN/50 Nm load cell, operating at less
than 1% accuracy within 10–100% loading capacity [24,25]. The setup with a specimen

</page>
<page number='4'>
Medicina 2023, 59, 1379
4 of 11
mounted for biomechanical testing is visualized in Figure 2. Each specimen was aligned
and tested in an upright standing position. The ilium part of the examined anatomical side
was ﬁxed to the base of the machine using a vice, gripping the part of the ilium between
the ramus and the border of the acetabulum. Two custom polymethylmethacrylate blocks
were modelled for repeated use, ensuring a standardized clamping force applied by the
vice on the clamped specimen region. Loading along the machine axis was applied to the
sacrum with 41 mm anterior offset relative to the posterior-superior S1 endplate aspect,
generating the required bending moment around the medio-lateral axis as calculated from
a previous inverse-dynamic gait analysis [19]. A custom steel plate with L-proﬁle was
used for this purpose. The sacrum was attached to the vertically oriented side of the plate
with two screws inserted through its fourth foramen. The horizontal part of the plate was
attached to the machine actuator through a cardan joint. Four retro-reﬂective marker sets
were attached to the sacrum, the iliac crest and both SI screws for optical motion tracking.
 
Figure 2. Setup with a specimen mounted for biomechanical testing. Vertical arrow indicates
loading direction.
The loading protocol was adopted identically from a previous study [26].
2.2. Data Acquisition & Analysis
Machine data in terms axial displacement and axial load were continuously obtained
from the machine transducer and the load cell throughout testing, respectively. On this
basis, construct stiffness was evaluated from the ascending load–displacement curve of the
initial quasi-static ramp.
The three-dimensional coordinates of all optical markers were continuously recorded
identically as described before [26]. Based on the motion tracking data, the following

</page>
<page number='5'>
Medicina 2023, 59, 1379
5 of 11
parameters of interest were evaluated: (1) gap angle, deﬁned as the combined angular
displacement of the sacrum in coronal and horizontal plane relative to the ilium; (2) ﬂexion,
deﬁned as the angular ﬂexion displacement of the sacrum relative to the ilium; (3) screw
tilt ilium, deﬁned as the angular displacement of the S1 screw relative to the ilium and
(4) screw tip cutout, deﬁned as the translational displacement of the S1 screw tip relative
to the sacrum in the plane perpendicular to the screw axis. The outcome measures were
evaluated at three time points of cyclic testing after 1000, 2000, and 3000 cycles, under
maximal load of the respective cycle and relative to the beginning of the cyclic test. The
latter number represented the highest rounded number of cycles when none of the spec-
imens had failed. Reaching 5◦gap angle was arbitrary set as a clinically relevant failure
criterion, and the corresponding number of cycles until its fulﬁllment under maximal load
of the corresponding cycle—deﬁned as cycles to failure—was calculated together with the
corresponding maximal load, deﬁned as load at failure.
Statistical analysis was performed with SPSS software (v.27, IBM SPSS, Armonk,
NY, USA). Normality of data distribution was screened and proved with Shapiro–Wilk
test. Signiﬁcant differences between the group pairs within each set (using same screw
design) regarding construct stiffness, cycles to failure and load at failure were detected with
Independent-Samples t-test. General Linear Model Repeated Measures test was conducted
to identify signiﬁcant differences between the group pairs within each set with regard to
the parameters of interest evaluated over the time points after 1000, 2000, and 3000 test
cycles. Level of signiﬁcance was set at 0.05 for all statistical tests.
3. Results
Construct stiffness was 47.0 ± 11.1 N/mm (mean value ± standard deviation, SD) in
group PT w/and 29.4 ± 7.4 N/mm in group PT w/o (set 1), 33.1 ± 8.2 N/mm in group FT
w/and 27.7 ± 9.7 N/mm in group FT w/o (set 2), and 31.9 ± 8.4 N/mm in group TS w/and
47.5 ± 18.7 N/mm in group TS w/o (set 3). Group PT w/was associated with signiﬁcantly
higher stiffness compared to group PT w/o, p = 0.012. No signiﬁcant differences were
detected between the other two pairs of groups with and without a washer in set 2 (FT
w/versus FT w/o) and set 3 (TS w/versus TS w/o), p ≥0.110.
The outcome measures analyzed over the three time points after 1000, 2000, and
3000 cycles are summarized in Table 1. Gap angle and screw tilt ilium were associated with
signiﬁcantly higher values in group FT w/o compared to its paired group FT w/, p ≤0.028.
Furthermore, ﬂexion trended towards higher values in group FT w/o compared to group
FT w/, p = 0.083, with no further signiﬁcant differences between the group pairs within
each set with regard to the two parameters of interest, p ≥0.121.
Table 1. Outcome measures evaluated after 1000, 2000 and 3000 cycles, presented for each group in
terms of mean value and SD, together with p-values from the statistical evaluation over cycles and
between the group pairs within each set.
Parameter
Group
Cycles
p-Value
Groups
1000
2000
3000
Gap angle (◦)
PT w/
0.50 (0.39)
0.84 (0.66)
1.19 (0.87)
0.751
PT w/o
0.47 (0.20)
0.92 (0.36)
1.45 (0.56)
FT w/
0.28 (0.30)
0.74 (0.50)
1.30 (0.65)
0.028
FT w/o
1.31 (0.49)
3.52 (2.04)
6.46 (4.47)
TS w/
2.68 (2.33)
3.67 (2.58)
4.84 (2.76)
0.236
TS w/o
1.26 (1.07)
2.26 (1.43)
3.23 (1.67)
p-value
over cycles
≤0.038

</page>
<page number='6'>
Medicina 2023, 59, 1379
6 of 11
Table 1. Cont.
Parameter
Group
Cycles
p-Value
Groups
1000
2000
3000
Flexion (◦)
PT w/
1.09 (1.31)
2.47 (2.27)
3.22 (2.61)
0.973
PT w/o
0.96 (0.30)
2.10 (0.71)
3.81 (0.77)
FT w/
0.87 (0.27)
1.80 (0.58)
2.90 (0.90)
0.083
FT w/o
3.32 (2.62)
6.03 (5.03)
9.91 (6.80)
TS w/
4.47 (3.24)
6.65 (4.13)
10.63 (5.94)
0.132
TS w/o
2.23 (1.77)
3.93 (2.62)
5.62 (3.53)
p-value
over cycles
≤0.042
Screw tilt ilium (◦)
PT w/
0.68 (0.57)
1.38 (0.88)
1.92 (1.02)
0.452
PT w/o
0.71 (0.13)
1.48 (0.27)
2.59 (0.27)
FT w/
0.50 (0.23)
1.13 (0.48)
1.87 (0.75)
0.011
FT w/o
2.12 (1.05)
5.25 (2.64)
9.34 (4.47)
TS w/
3.17 (2.24)
4.73 (2.78)
7.26 (3.87)
0.232
TS w/o
1.88 (1.25)
3.30 (1.82)
4.75 (2.29)
p-value
over cycles
≤0.011
Screw tip cutout (mm)
PT w/
0.12 (0.07)
0.23 (0.18)
0.28 (0.22)
0.139
PT w/o
0.09 (0.07)
0.23 (0.15)
0.60 (0.09)
FT w/
0.17 (0.09)
0.35 (0.08)
0.37 (0.22)
0.121
FT w/o
0.54 (0.48)
0.98 (1.02)
1.76 (1.27)
TS w/
0.57 (0.37)
1.33 (0.90)
2.96 (2.02)
0.742
TS w/o
0.89 (1.05)
1.51 (1.29)
1.82 (1.96)
p-value
over cycles
≥0.216 (PT w/, FT/w, TS/w)
≤0.023 (PT w/o, FT w/o, TS w/o)
PT w/and PT w/o: groups with partially threaded short screws with and without washers; FT w/and FT w/o:
groups with fully threaded short screws with and without washers; TS w/and TS w/o: groups with fully threaded
long transsacral screws with and without washers
Cycles to failure and load at failure were 5452 ± 944/694.3 ± 47.2 N in group PT w/and
5016 ± 531/450.8 ± 26.6 N in group PT w/o (set 1), 3972 ± 600/398.6 ± 30.0 N in group FT
w/and 2993 ± 527/349.7 ± 26.4 N in group FT w/o (set 2), and 3189 ± 1674/359.5 ± 83.7 N
in group TS w/and 3630 ± 348/381.5 ± 17.4 N in group TS w/o (set 3), respectively. Group
FT w/was associated with significantly higher values for both of these parameters of interest
compared to group FT w/o, p = 0.026 (Figure 3). No significant differences were detected
between the other two pairs of groups with and without a washer in set 1 (PT w/versus PT
w/o) and set 3 (TS w/versus TS w/o), p ≥0.359. Failure modes for all fixation methods were
expressed by a fracture of the ilium between the polymethylmethacrylate ilium fixation and
the S2 SI screw.

</page>
<page number='7'>
Medicina 2023, 59, 1379
7 of 11
Figure 3. Cycles to failure (left abscissa) and corresponding load at failure (right abscissa), presented
for each separate group in terms of mean value and SD. Star indicates signiﬁcant differences between
the groups.
4. Discussion
The goal of this study was to assess the stability of standard S1-S2 SI screw ﬁxations,
with and without using a washer, across different screw designs. It was hypothesized that
in good bone quality the omission of the washer would result in equivalent biomechanical
stability. The following two main important points can be identiﬁed:
1.
Partially threaded short and fully threaded long transsacral screws demonstrated
equivalent biomechanical stability under dynamic loading disregarding whether
a washer was used or not.
2.
Omission of the washer led to a signiﬁcantly diminished biomechanical stability under
dynamic loading with fully threaded short screws.
The surgical therapy of the qualiﬁed groups in the presented study is regularly used
in clinical practice [27–29]. However, previous work could not reveal signiﬁcant differences
between the different types of SI screw ﬁxation [27,30,31]. In contrast, the experimental set-
ting in the current investigation seems to be relevant to detect even the smallest differences
in biomechanical behavior between the groups, such as the choice of washer inclusion.
The routine use of a washer for ﬁxation of the posterior pelvis ring seems to be at
the discretion of the treating surgeon and is scarcely discussed in the current literature.
Therefore, an investigation is clearly difﬁcult due to the lack of studies. A recent review and
expert opinion concerning transsacral screw ﬁxation of posterior pelvis ring injuries does
not cover this topic in any manner and only devotes a single sentence to it: “We routinely
utilize a washer if there is fracture displacement” [6,32].
A comparable study, using fully threaded 7.3 mm sacroiliac S1 screws, described
washer penetration in the iliac bone [19]. In our study, no penetration of the screw heads
or washers into the cortices of the bone model occurred in any group. According to
the operator’s judgement, the screws with and without washer could be tightened with
comparable strength. This seems to be reﬂected in the results with comparable initial
construct stiffness between the ﬁxations using the same screw design with and without
a washer, yet with signiﬁcantly higher stiffness in group PT w/versus group PT w/o.
Characteristically, the initial stiffness of partially threaded screws with a washer was
higher, although this supposed advantage seems to be eliminated during dynamic loading,
at least to the point where the screw head eventually breaks into the cortex. With fully
threaded short screws on the other hand, it was demonstrated that although the initial
stiffness was comparable, the advantages of using a washer only become apparent during
dynamic loading.

</page>
<page number='8'>
Medicina 2023, 59, 1379
8 of 11
Washers are known as safeguards against screw intrusion as well as a technique
to retain compressive force after screw intrusion [6]. Furthermore, they are a standard
component in the iliosacral screw placement recommendations from the AO [22]. Yet,
there is little data on over-compression of the SI joints in the literature. Most authors
merely describe that this should be avoided [32–34]. It has further been reported as
a disadvantage that ﬁxation of posterior SI joint dislocations with transiliac sacral bars,
including over-compression of the ilium, may lead to damage to the sacral nerves [35].
A different study regarding this topic recommends cannulated 7.3 mm partially threaded
screws with a washer, however, fully threaded washerless screws may be preferred to avoid
over-compression of a sacral fracture in case of comminution [34].
A transiliac ﬁxator for treatment of comminuted sacrum fractures has the potential for
higher stiffness with a lower risk of over-compression [36]. However, judging the quality
of reduction is difﬁcult and there is a risk of over-compression with nerve injury when
a sacral fracture is present [37].
The amount of applied compression seems to be left to the experience of the surgeon.
The judgement of the treating operator should be utilized to avoid over-compression of the
fracture of the posterior pelvis ring [32]. The same competence should be attributed with
regard to screw intrusion. In addition, this previous investigation found that there were
no signiﬁcant differences between the treatment groups in terms of gap angle and screw
tilt in the ilium, suggesting that in young patients, the exclusion of the washer seems to be
feasible. However, the current study demonstrated signiﬁcantly higher values for these
two parameters of interest (gap angle and screw tilt in ilium) in group FT w/o compared
to group FT w/. In addition, the number of cycles to failure and load at failure were
signiﬁcantly higher in the latter versus the former group. In our test setup, the symphysis
was not ﬁxed, as it might happen in a clinical situation [3].
A biomechanical study investigating cement augmentation of SI screws concluded that
bilateral bone implant anchorage was the signiﬁcantly more important factor concerning
fracture displacement than the actual number of inserted screws [37]. It has further been
stated that longer screws achieve higher stability than shorter screws [3].
Strength & Limitations
The obvious limitation of this investigation is the chosen artiﬁcial bone model. This
makes the simulation of ligament injuries of the pelvis, as well as screw intrusion, difﬁcult.
Though, as this is an innovative study with a debatable approach, for which there is limited
data available and an unpredictable outcome, the authors agreed to the artiﬁcial specimens
as a ﬁrst step approach. Following a successful ﬁrst artiﬁcial bone study, it is ethically
acceptable to proceed with a cadaver investigation. Further, the investigated injury was
purposely chosen to provide an absolute unstable situation representing the worst-case
scenario. Therefore, the missing ligaments in the chosen specimens could be disregarded
in the performed test series.
Furthermore, artificial pelvises allow standardized experimental groups, which can
overpower innumerable differences in the bone quality of human cadavers and are also more
cost-effective [38–41]. Specifically, when investigating the pelvis, artificial bone specimens
have been repeatedly and effectively used in many biomechanical studies [31,38,42–44].
Moreover, the accessibility of cadavers is not only limited, but the specimens are also costly,
both of which can influence the sample size of biomechanical research. It is already recognized
that the sample sizes used in earlier publications are in general small [45]. While the sample
size in this investigation was moderately small, it is equivalent to comparable biomechanical
studies investigating posterior pelvis fixation techniques [31,42–44,46]. Missing torque data on
the tightening force of the screws with and without washers is another limitation. However,
since all screws were implanted by the same experienced surgeon and there was no screw
head or washer penetration into the bone, it can be assumed that all screws were tightened
with a comparable strength. Finally, the witnessed failure modes, fracturing of the ilium in
between the ilium fixation and S2 SI screw, seem to be far from clinically relevancy, especially

</page>
<page number='9'>
Medicina 2023, 59, 1379
9 of 11
for young patients. Therefore, the bones used may not have been able to properly simulate
certain screw loosening effects, e.g., cut-through of the proximal screw part into the cortex.
Nevertheless, the knowledge gained can serve as a basis for further research on different bone
models or cadaveric bones.
5. Conclusions
From a biomechanical perspective, a washer could be optional when using partially
threaded short or fully threaded long transsacral S1-S2 screws for treatment of posterior pelvis
ring injuries in young trauma patients. Yet, the omission of the washer in fully threaded
short screws could lead to a significantly diminished biomechanical stability. Additional
biomechanical cadaveric studies should be initiated for a reliable interpretation of washerless
fixations and their potential for the therapy of the injured posterior pelvis ring.
Author Contributions: Conceptualization, T.B., T.P., S.H., B.G. and H.-C.P.; methodology, T.B., P.S.,
B.G. and H.-C.P.; data collection, T.B., I.Z. and T.P.; analysis, I.Z., P.S., S.H. and T.P.; writing—original
draft preparation, T.B., I.Z., P.S. and S.H.; writing—review and editing, T.P., S.H., G.R. and B.G.;
supervision, G.R., B.G. and H.-C.P.; project administration, T.B., G.R., B.G. and H.-C.P. All authors
have read and agreed to the published version of the manuscript.
Funding: No external funding sources were utilized to conduct and complete this study.
Data Availability Statement: The datasets analyzed during this study are available from correspond-
ing author upon reasonable request.
Acknowledgments: The authors are not compensated and there are no other institutional subsidies,
corporate afﬁliations, or funding sources supporting this work unless clearly documented and
disclosed. This investigation was performed with the assistance of the AO Foundation.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
References
1.
Chip, M.C., Jr.; Simonian, P.T.; Agnew, S.G.; Mann, F.A. Radiographic recognition of the sacral alar slope for optimal placement of
iliosacral screws: A cadaveric and clinical study. J. Orthop. Trauma 1996, 10, 171–177. [CrossRef] [PubMed]
2.
Teo, A.Q.A.; Yik, J.H.; Keat, S.N.J.; Murphy, D.P.; O’Neill, G.K. Accuracy of sacroiliac screw placement with and without
intraoperative navigation and clinical application of the sacral dysmorphism score. Injury 2018, 49, 1302–1306. [CrossRef]
[PubMed]
3.
Van Zwienen, C.M.A.; van den Bosch, E.W.; Snijders, C.J.; Kleinrensink, G.J.; van Vugt, A.B. Biomechanical comparison of
sacroiliac screw techniques for unstable pelvic ring fractures. J. Orthop. Trauma 2004, 18, 589–595. [CrossRef]
4.
Dilogo, I.H.; Satria, O.; Fiolin, J. Internal ﬁxation of S1-S3 iliosacral screws and pubic screw as the best conﬁguration for
unstable pelvic fracture with unilateral vertical sacral fracture (AO type C1.3): A biomechanical study. J. Orthop. Surg. 2017,
25, 2309499017690985. [CrossRef] [PubMed]
5.
Johnson, N.L.; Galuppo, L.D.; Stover, S.M.; Taylor, K.T. An in vitro biomechanical comparison of the insertion variables and
pullout mechanical properties of AO 6.5-mm standard cancellous and 7.3-mm self-tapping, cannulated bone screws in foal
femoral bone. Vet. Surg. 2004, 33, 691–698. [CrossRef]
6.
Bishop, J.A.; Behn, A.W.; Castillo, T.N. The Biomechanical Signiﬁcance of Washer Use with Screw Fixation. J. Orthop. Trauma 2014,
28, 114–117. [CrossRef]
7.
Yücel, N.; Lefering, R.; Tjardes, T.; Korenkov, M.; Schierholz, J.; Tiling, T.; Bouillon, B.; Rixen, D. Is implant removal after
percutaneous iliosacral screw ﬁxation of unstable posterior pelvic ring disruptions indicated? Unfallchirurg 2004, 107, 468–474.
8.
Gansslen, A.; Hufner, T.; Krettek, C. Percutaneous iliosacral screw ﬁxation of unstable pelvic injuries by conventional ﬂuoroscopy.
Oper. Orthop. Traumatol. 2006, 18, 225–244. [CrossRef]
9.
Peng, K.T.; Huang, K.C.; Chen, M.C.; Li, Y.Y.; Hsu, R.W.W. Percutaneous placement of iliosacral screws for unstable pelvic ring
injuries: Comparison between one and two C-arm ﬂuoroscopic techniques. J. Trauma-Inj. Infect. Crit. Care 2006, 60, 602–608.
[CrossRef]
10.
Schweitzer, D.; Zylberberg, A.; Cordova, M.; Gonzalez, J. Closed reduction and iliosacral percutaneous ﬁxation of unstable pelvic
ring fractures. Inj.-Int. J. Care Inj. 2008, 39, 869–874. [CrossRef]
11.
Routt, M.C., Jr.; Simonian, P.T.; Mills, W.J. Iliosacral screw ﬁxation: Early complications of the percutaneous technique. J. Orthop.
Trauma 1997, 11, 584–589. [CrossRef] [PubMed]
12.
Richards, R.; Palmer, J.; Clarke, N. Observations on removal of metal implants. Injury 1992, 23, 25–28. [CrossRef] [PubMed]
13.
Schmalzried, T.P.; Grogan, T.J.; Neumeier, P.A.; Dorey, F.J. Metal removal in a pediatric population: Benign procedure or necessary
evil? J. Pediatr. Orthop. 1991, 11, 72–76. [CrossRef]

</page>
<page number='10'>
Medicina 2023, 59, 1379
10 of 11
14.
Stuby, F.; Gonser, C.; Baron, H.; Stöckle, U.; Badke, A.; Ochs, B. Hardware removal after pelvic ring injury. Unfallchirurg 2012, 115,
330–338. [CrossRef] [PubMed]
15.
Culemann, U.; Tosounidis, G.; Reilmann, H.; Pohlemann, T. Pelvic fracture. Diagnostics and current treatment options. Un-
fallchirurg 2004, 107, 1169–1181.
16.
Langﬁtt, M.K.; Best, B.J.; Carroll, E.A. A useful tool for retained washer retrieval when removing iliosacral screws. J. Surg. Orthop.
Adv. 2013, 22, 330–332. [CrossRef]
17.
Osterhoff, G.; Noser, J.; Sprengel, K.; Simmen, H.-P.; Werner, C.M. Rate of intraoperative problems during sacroiliac screw
removal: Expect the unexpected. BMC Surg. 2019, 19, 39. [CrossRef] [PubMed]
18.
Oberst, M.; Konrad, G.; Herget, G.W.; El Tayeh, A.; Suedkamp, N.P. Novel endoscopic sacroiliac screw removal technique:
Reduction of intraoperative radiation exposure. Arch. Orthop. Traum Surg. 2014, 134, 1557–1560. [CrossRef] [PubMed]
19.
Grüneweller, N.; Raschke, M.J.; Zderic, I.; Widmer, D.; Wähnert, D.; Gueorguiev, B.; Richards, R.G.; Fuchs, T.; Windolf, M.
Biomechanical comparison of augmented versus non-augmented sacroiliac screws in a novel hemi-pelvis test model. J. Orthop.
Res. 2017, 35, 1485–1493. [CrossRef]
20.
Gueorguiev, B.; Ockert, B.; Schwieger, K.; Wähnert, D.; Lawson-Smith, M.; Windolf, M.; Stoffel, K. Angular stability potentially
permits fewer locking screws compared with conventional locking in intramedullary nailed distal tibia fractures: A biomechanical
study. J. Orthop. Trauma 2011, 25, 340–346. [CrossRef]
21.
Burgess, A.R.; Eastridge, B.J.; Young, J.W.; Ellison, T.S.; Ellison, P.S., Jr.; Poka, A.; Bathon, G.H.; Brumback, R.J. Pelvic ring
disruptions: Effective classiﬁcation system and treatment protocols. J. Trauma Acute Care 1990, 30, 848–856. [CrossRef]
22.
Nambiar, M.; West, L.R.; Bingham, R. AO Surgery Reference: A comprehensive guide for management of fractures. Br. J. Sport.
Med. 2017, 51, 545–546. [CrossRef]
23.
Berk, T.; Zderic, I.; Varga, P.; Schwarzenberg, P.; Lesche, F.; Halvachizadeh, S.; Richards, G.; Gueorguiev, B.; Pape, H.-C. Evaluation
of Cannulated Compression Headless Screw (CCHS) as an alternative implant in comparison to standard S1–S2 screw ﬁxation of
the posterior pelvis ring: A biomechanical study. BMC Musculoskelet. Disord. 2023, 24, 215. [CrossRef]
24.
Din, E. 376: 2011–09: Metallic Materials-Calibration of Force-Proving Instruments Used for the Veriﬁcation of Uniaxial Testing Machines;
Beuth: Berlin, Germany, 2011.
25.
ISO E 7500–1.
CEN EN ISO 7500–1; Metallic Materials-Veriﬁcation of Static Uniaxial Testing Machines-Part 1:
Ten-
sion/Compression Testing Machines-Veriﬁcation and Calibration of the Force-Measuring System.
European Committee
for Standardization: Brussels, Belgium, 2004.
26.
Berk, T.; Zderic, I.; Schwarzenberg, P.; Halvachizadeh, S.; Teuben, M.; Richards, G.; Gueorguiev, B.; Pape, H.-C. Cerclage
augmentation of S1–S2 trans-sacral screw ﬁxation in osteoporotic posterior pelvis ring injuries-a biomechanical feasibility study.
J. Orthop. Res. 2023. [CrossRef] [PubMed]
27.
Suzuki, T.; Hak, D.J.; Ziran, B.H.; Adams, S.A.; Stahel, P.F.; Morgan, S.J.; Smith, W.R. Outcome and complications of posterior
transiliac plating for vertically unstable sacral fractures. Inj.-Int. J. Care Inj. 2009, 40, 405–409. [CrossRef] [PubMed]
28.
Berber, O.; Amis, A.A.; Day, A.C. Biomechanical testing of a concept of posterior pelvic reconstruction in rotationally and
vertically unstable fractures. J. Bone Jt. Surg. -Br. Vol. 2011, 93B, 237–244. [CrossRef]
29.
Grifﬁn, D.R.; Starr, A.J.; Reinert, C.M.; Jones, A.L.; Whitlock, S. Vertically unstable pelvic fractures ﬁxed with percutaneous
iliosacral screws: Does posterior injury pattern predict ﬁxation failure? J. Orthop. Trauma 2006, 20, S30–S36. [CrossRef] [PubMed]
30.
Vigdorchik, J.M.; Esquivel, A.O.; Jin, X.; Yang, K.H.; Onwudiwe, N.A.; Vaidya, R. Biomechanical stability of a supra-acetabular
pedicle screw Internal Fixation device (INFIX) vs External Fixation and plates for vertically unstable pelvic fractures. J. Orthop.
Surg. Res. 2012, 7, 1–6. [CrossRef] [PubMed]
31.
Yinger, K.; Scalise, J.; Olson, S.A.; Bay, B.K.; Finkemeier, C.G. Biomechanical comparison of posterior pelvic ring ﬁxation. J. Orthop.
Trauma 2003, 17, 481–487. [CrossRef]
32.
Ziran, N.; Collinge, C.A.; Smith, W.; Matta, J.M. Trans-sacral screw ﬁxation of posterior pelvic ring injuries: Review and expert
opinion. Patient Saf. Surg. 2022, 16, 24. [CrossRef]
33.
Kregor, P.; Routt, M.C., Jr. Unstable pelvic ring disruptions in unstable patients. Injury 1999, 30, 19–28. [CrossRef] [PubMed]
34.
Ali, E.; Al-AShab, M.; Kandil, M.; Sholah, S.; Fathi, M. Management of Sacral and Sacroiliac Joint Fractures by Percutaneous
Screws. Benha J. Appl. Sci. 2021, 6, 197–205. [CrossRef]
35.
Gänsslen, A.; Pohlemann, T.; Krettek, C. Internal ﬁxation of sacroiliac joint disruption. Oper. Orthop. Und Traumatol. 2005, 17,
281–295. [CrossRef]
36.
Salasek, M.; Jansova, M.; Kˇren, J.; Pavelka, T.; Weisova, D. Biomechanical comparison of a transiliac internal ﬁxator and two
iliosacral screws in transforaminal sacral fractures: A ﬁnite element analysis. Acta Bioeng. Biomech. 2015, 17, 39–49.
37.
Farouk, O.; Farouk, A.P.O. Closed reduction and percutaneous iliosacral screw ﬁxation of sacroiliac injuries: Surgical technique
and outcome. J. Orthop. 2007, 4, e26.
38.
Gardner, M.P.; Chong, A.; Pollock, A.G.; Wooley, P.H. Mechanical evaluation of large-size fourth-generation composite femur and
tibia models. Ann. Biomed. Eng. 2010, 38, 613–620. [CrossRef]
39.
Heiner, A.D. Structural properties of fourth-generation composite femurs and tibias. J. Biomech. 2008, 41, 3282–3284. [CrossRef]
40.
Zdero, R.; Olsen, M.; Bougherara, H.; Schemitsch, E. Cancellous bone screw purchase: A comparison of synthetic femurs, human
femurs, and ﬁnite element analysis. Proc. Inst. Mech. Eng. Pt H J. Eng. Med. 2008, 222, 1175–1183. [CrossRef] [PubMed]

</page>
<page number='11'>
Medicina 2023, 59, 1379
11 of 11
41.
Elfar, J.; Stanbury, S.; Menorca, R.M.G.; Reed, J.D. Composite bone models in orthopaedic surgery research and education. J. Am.
Acad. Orthop. Surg. 2014, 22, 111.
42.
Camino Willhuber, G.; Zderic, I.; Gras, F.; Wahl, D.; Sancineto, C.; Barla, J.; Windolf, M.; Richards, R.G.; Gueorguiev, B. Analysis of
sacro-iliac joint screw ﬁxation: Does quality of reduction and screw orientation inﬂuence joint stability? A biomechanical study.
Int. Orthop. 2016, 40, 1537–1543. [CrossRef]
43.
Gardner, M.J.; Kendoff, D.; Ostermeier, S.; Citak, M.; Hüfner, T.; Krettek, C.; Nork, S.E. Sacroiliac joint compression using
an anterior pelvic compressor: A mechanical study in synthetic bone. J. Orthop. Trauma 2007, 21, 435–441. [CrossRef] [PubMed]
44.
Sahin, O.; Demirors, H.; Akgun, R.; Tuncay, I. Internal ﬁxation of bilateral sacroiliac dislocation with transiliac locked plate:
A biomechanical study on pelvic models. Acta Orthop. Traumatol. Turc. 2013, 47, 411–416. [CrossRef] [PubMed]
45.
Sagi, H.; Ordway, N.; DiPasquale, T. Biomechanical analysis of ﬁxation for vertically unstable sacroiliac dislocations with iliosacral
screws and symphyseal plating. J. Orthop. Trauma 2004, 18, 138–143. [CrossRef]
46.
Van Zwienen, C.M.A.; van den Bosch, E.W.; van Dijke, G.A.H.; van Vugt, A.B. Cyclic loading of sacroiliac screws in tile C pelvic
fractures. J. Trauma-Inj. Infect. Crit. Care 2005, 58, 1029–1034. [CrossRef] [PubMed]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

</page>
</source_document>

<source_document id='Cher 2015.pdf' author='Cher' year='2015'>
<page number='1'>
Medical Devices: Evidence and Research
ISSN: 1179-1470 (Online) Journal homepage: www.tandfonline.com/journals/dmde20
Implant survivorship analysis after minimally
invasive sacroiliac joint fusion using the iFuse
Implant System®
Daniel J Cher, W Carlton Reckling & Robyn A Capobianco
To cite this article: Daniel J Cher, W Carlton Reckling & Robyn A Capobianco (2015) Implant
survivorship analysis after minimally invasive sacroiliac joint fusion using the iFuse Implant
System®, Medical Devices: Evidence and Research, , 485-492, DOI: 10.2147/MDER.S94885
To link to this article:  https://doi.org/10.2147/MDER.S94885
© 2015 Cher et al. This work is published by
Dove Medical Press Limited, and licensed
under Creative Commons Attribution – Non
Commercial (unported, v3.0) License
Published online: 23 Nov 2015.
Submit your article to this journal 
Article views: 210
View related articles 
View Crossmark data
Citing articles: 3 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=dmde20

</page>
<page number='2'>
© 2015 Cher et al. This work is published by Dove Medical Press Limited, and licensed under Creative Commons Attribution – Non Commercial (unported, v3.0) 
License. The full terms of the License are available at http://creativecommons.org/licenses/by-nc/3.0/. Non-commercial uses of the work are permitted without any further 
permission from Dove Medical Press Limited, provided the work is properly attributed. Permissions beyond the scope of the License are administered by Dove Medical Press Limited. Information on 
how to request permission may be found at: http://www.dovepress.com/permissions.php
Medical Devices: Evidence and Research 2015:8 485–492
Medical Devices: Evidence and Research
Dovepress
submit your manuscript | www.dovepress.com
Dovepress 
485
O r i g i n a l  R e s e a r c h
open access to scientific and medical research
Open Access Full Text Article
http://dx.doi.org/10.2147/MDER.S94885
Implant survivorship analysis after minimally 
invasive sacroiliac joint fusion using the iFuse 
Implant System®
Daniel J Cher1
W Carlton Reckling2
Robyn A Capobianco1
1Department of Clinical Affairs, 
SI-BONE, Inc., 2Department of 
Medical Affairs, SI-BONE, Inc., 
San Jose, CA, USA
Correspondence: Daniel Cher
Department of Clinical Affairs, SI-BONE, 
3055 Olin Avenue Suite 2200, San Jose, 
CA 95128, USA
Tel +1 650 269 5763
Email dcher@si-bone.com
Introduction: Surgical revision rate is a key outcome with all permanent implants. The iFuse 
Implant System® is a permanent implant used to perform minimally invasive sacroiliac joint 
fusion. The purpose of this study is to determine the surgical revision rate after sacroiliac joint 
fusion surgery with this system.
Methods: Using two internal sources of information, revision surgeries were identified and 
linked to index surgeries. The likelihood of revision surgery was calculated using the Kaplan–
Meier life table approach. Predictors of revision were explored.
Results: Four-year survivorship free from implant revision was 96.46%. Revision rate did 
not differ by sex and was lower for age .65. In all, 24% of revisions occurred within the first 
30 days after surgery; 63.5% occurred within year 1. Implant survivorship has improved annu­
ally since the device was introduced in 2009.
Conclusion: The survivorship rate with this implant is high and improving; the rate is somewhat 
higher than total hip replacement but lower than that of lumbar spine procedures.
Keywords: safety, sacroiliac joint fusion, iFuse Implant System, revision
Introduction
The safety and effectiveness of devices used to treat medical conditions are of key 
concern to physicians, patients, and payors. Several regulatory pathways are available 
for the commercialization of medical devices in the US. In some cases, devices may 
be commercialized without the need for premarket clinical data. Even when premarket 
clinical data are required, trial sample sizes may be too small to detect rare events. 
Consequently, the US Food and Drug Administration (FDA) requires postmarket 
surveillance to maintain a reasonable assurance of safety for all medical devices.
Key components of postmarket surveillance include complaint handling1 and 
reporting of events through the Medical Device Reporting regulation (Code of Federal 
Regulations, Title 21, Part 803).2 The former requires a manufacturer to maintain a 
record of all complaints of which the manufacturer becomes aware. Complaints are 
defined broadly as any “communication that alleges deficiencies related to the identity, 
quality, durability, reliability, safety, effectiveness or performance” of the device.2 The 
latter requires manufacturers, importers, and device user facilities (eg, hospitals, sur­
gical facilities, and other health care sites of service) to report certain device-related 
adverse events as well as product issues (ie, complaints) to the US FDA.
Postmarket tracking of medical device complaints and adverse events can help to 
uncover risks not foreseen or not quantifiable in the premarket setting.3 Data reported 
through both of these systems have led to the detection of unanticipated complications 
Number of times this article has been viewed
This article was published in the following Dove Press journal: 
Medical Devices: Evidence and Research
23 November 2015

</page>
<page number='3'>
Medical Devices: Evidence and Research 2015:8
submit your manuscript | www.dovepress.com
Dovepress 
Dovepress
486
Cher et al
associated with total hip arthroplasty,4 a pelvic mesh,5,6 
uterine fibroid tumor ablation procedures,7 and mechanical 
heart valves.8
Sacroiliac (SI) joint disorders are a well-known medi­
cal condition with both surgical and nonsurgical treatment 
options. Until recently, surgical options have involved decor­
tication of the SI joint and permanent fixation using screws 
and plates during an open surgical procedure.9 More recently, 
several devices for minimally invasive SI joint fusion have 
become commercially available. Most of the published litera­
ture reports the use of the iFuse Implant System® (SI-BONE, 
Inc., San Jose, CA, USA). The iFuse Implant System includes 
a delivery system to place a series of triangular titanium 
implants coated with a porous titanium plasma spray across 
the SI joint using a lateral, transarticular approach under 
fluoroscopic guidance.10 In the US, iFuse Implant System 
is intended for sacroiliac fusion for conditions including 
sacroiliac joint dysfunc­tion that is a direct result of sacroiliac 
joint disruption and degenerative sacroiliitis. This includes 
conditions in which symptoms began during pregnancy or in 
the peripartum period and have persisted postpartum for more 
than 6 months. In other geographies, iFuse Implant System is 
indicated for sacroiliac joint fusion. Placement of the implants 
does not require full decortication of the joint, as is done in 
other joint fusion procedures. The implant’s shape allows for 
immediate stabilization of the joint and the titanium plasma 
spray coating allows for biologic fixation in bone.
As with other permanent implants placed surgically, the 
rate of surgical revision is a key outcome. Revision surgery 
in patients who undergo iFuse implant placement can occur 
early, typically as a result of neural impingement due to 
malposition, or late due to persistent or recurrent pain. Late 
pain could be due to implant loosening or failure to achieve 
bony fusion. Revision surgery can entail implant removal or 
repositioning, as well as placement of additional implants or 
other types of interventions.
Revision after minimally invasive SI joint fusion using 
the iFuse Implant System appears to be uncommon in both 
mid- and long-term published case series,11–15 as well as in 
two recently completed multi-center prospective trials.16,17 An 
accurate estimate of the revision rate, as well as monitoring 
any changes in the rate, requires a large number of patients 
and extended follow-up. In this report, we combine informa­
tion from company-maintained inventory management and 
complaints databases to estimate the revision rate after SI joint 
fusion. We compare the revision rate observed in the commer­
cial setting to those reported in two ongoing prospective clini­
cal trials (INSITE: NCT01681004, and SIFI: NCT01640353), 
as well as to rates reported with other orthopedic implants.
Methods
Two databases were used for the current analysis: inventory 
management and complaints. Since 2009, key data captured for 
surgeries using the iFuse Implant System have been recorded in 
an inventory database. These elements include a unique iden­
tifier, procedure date, institution, operating surgeon, implant 
catalog and lot number, and patient sex and age.
In addition, as part of standard postmarket surveillance, 
the company records and investigates all reported complaints 
related to the device, regardless of source or mechanism 
of communication, and stores this information in a data­
base.1 Received complaints are individually evaluated for 
reportability as required by the US FDA’s Medical Device 
Reporting regulation as well as international regulations.2 
Institutional review board approval was not required for this 
study as it was based on an analysis of internal company data 
routinely collected during postmarket surveillance.
Each complaint was manually reviewed and classified 
according to whether or not it represented a surgical revision. 
When further information was required, the operating physi­
cian was contacted by telephone or email. For the purpose 
of this study, a revision is defined as the occurrence of an 
additional surgical procedure on an SI joint treated with the 
iFuse Implant System for primary SI joint fusion. Index cases 
that were inconsistent with the device’s labeled instructions 
for use (eg, revision of a failed primary SI joint procedure 
that used a different implant system) were excluded prior to 
analysis. Types of revision procedures included: a removal or 
repositioning of the originally placed implant(s), placement 
of additional implant(s), the use of non-iFuse implants to 
provide additional fixation of the originally treated joint, or 
the surgical debridement and grafting of the SI joint with or 
without changes to any of the implants. Each revision case 
in the complaints database was then manually linked to the 
corresponding index (ie, initial) surgery in the inventory-
tracking database.
The likelihood of revision after surgery was calculated 
using the Kaplan–Meier life table approach. Time to revi­
sion was calculated as the difference in dates between the 
index surgery and the first revision surgery. For analysis 
purposes, inventory data were censored as of July 15, 2014. 
Follow-up was censored as of July 15, 2015. This ensured 
that all treated patients had at least 1-year follow-up. Patient 
vital status information was not available and not collected; 
therefore, survivorship rates do not account for death due 
to other causes. Given the relatively young mean age of 
patients undergoing this procedure (55.8), expected overall 
survival is high and lack of vital status information is not 
expected to meaningfully affect calculated rates. Analysis 

</page>
<page number='4'>
Medical Devices: Evidence and Research 2015:8
submit your manuscript | www.dovepress.com
Dovepress 
Dovepress
487
Implant survivorship analysis of iFuse Implant System®
was done on a per-side treated basis in order to accurately 
account for the small number of simultaneous bilateral 
surgeries. The proportion of simultaneous second sides was 
low (432/10,956; 3.9%). In five cases, a surgeon who had not 
performed the initial surgery performed the revision surgery 
and was unable to provide information on the surgeon who 
performed the index surgery. These cases were excluded, 
which results in a slight underestimate of the revision rate 
(see “Results” section). Revision surgeries were classified 
by cause: 1) symptomatic malposition (SM), 2) symptom 
recurrence (SR), with or without implant loosening, 3) per­
sistent pain, 4) infection, 5) fracture, or 6) early revision for 
asymptomatic implant malposition.
Differences in time to revision were compared using the 
log-rank statistic. Subgroup analyses were performed: patient 
age (by decades), sex, unilateral or bilateral surgery, year index 
surgery was performed, and surgeon. For the purposes of this 
analysis, bilateral surgery is used to describe fusion of both SI 
joints in the same surgery and does not include patients who 
underwent staged bilateral surgery where the two SI joints are 
fused in separate surgeries. When subgroup information was 
unavailable, analyses excluded missing values.
Of interest were reasons for changes in revision rates over 
time. Minimally invasive spinal surgery is known to have 
a learning curve; perioperative metrics and complications 
improve with experience.18 We examined surgeon learning 
curve using two methods. First, we ordered surgeon experi­
ence by case number (ie, 1st, 2nd, 3rd … 150th case, etc). 
Among surgeons who had performed at least 100 cases, we 
determined whether the likelihood of revision decreased with 
increased experience (grouping cases by case number: 1–20, 
21–50, 51–100, or .100) with the surgery/device. Second, 
for surgeons who had performed at least 20 cases, we exam­
ined revision rates in the first 20 cases over time categorized 
according to the year the surgeon’s first case was performed. 
Observed improvement over time in this second analysis 
could be attributed in part to improved training.
For the per-surgeon analysis, significant differences seen 
as a result of the log-rank test were investigated further as 
follows. The ratio of observed cases to expected cases (an 
output parameter of the log-rank test) was determined. Since 
random sampling alone can cause an elevated observed/
expected ratio, the lower confidence limit of the ratio was 
calculated using an exact Poisson method.19 Surgeons with 
observed/expected ratios whose lower confidence limit 
exceeded 1 were tabulated.
All analyses focused on surgeries and revisions in the US 
only. Since the number of surgeries performed in 2009 was 
small, revision rates are not reported beyond 4 years. The 
revision rate observed in the entire database was compared 
with revisions occurring during two ongoing prospective 
clinical trials (Sacroiliac Joint Fusion With iFuse Implant 
System, SIFI, NCT01640353 and Investigation of Sacroiliac 
Fusion Treatment, INSITE, NCT01681004) as well as several 
retrospective studies reported in the literature.11,12,21,22
All calculations were performed using R.20 Exact Poisson 
tests were performed using the “exactci” package (version 
1.3-1, http://cran.r-project.org/web/packages/exactci/exactci.
pdf).
Results
Between April 2009 and July 15, 2014, 11,416 cases of MIS SI 
joint fusion with iFuse Implant System took place in the US. 
Of these, 28 were excluded because their use was inconsistent 
with the manufacturer’s instructions for use. Of the 11,388 
remaining, 10,956 (96.2%) cases were unilateral, 432 (3.8%) 
cases were simultaneous bilateral (ie, both sides treated in the 
same operation), resulting in a total of 11,820 sides treated.
Patients who underwent SI joint fusion using the iFuse 
implant were predominantly female (58.9%, Table 1); mean 
age was 55.8 and 22% were over the age of 65. The number of 
surgeries performed increased per year. In the majority of uni­
lateral cases (89.6%), three implants were used. Similarly, six 
implants (three per side) were used in 87% of bilateral cases.
During the estimated 336,332 patient-side-months 
(28,027 patient-side-years) of follow-up, 320 revisions 
occurred. In five cases, the revision surgery could not be 
linked to a particular index surgery. Overall, 24% of revi­
sion surgeries occurred in the first month and 63% occurred 
within the first 12 months (Table 2).
The 4-year survival rate free from revision surgery was 
96.46% (cumulative revision rate of 3.54%). Adjusting for 
the inability to match five revision cases to index surger­
ies, the adjusted 4-year survival rate was 96.40% (adjusted 
revision rate of 3.60%). The revision rate improved substan­
tially over time (log-rank P,0.0001, Figure 1), with 1-year 
revision rates of 9.7%, 4.9%, 2.0%, 1.8%, 1.5%, and 1.4% 
during 2009, 2010, 2011, 2012, 2013, and 2014, respectively 
(P,0001). Because revision rates have fallen over time, the 
observed 4-year revision rate (3.55%) probably overestimates 
the actual current 4-year rate.
The most common reasons for revision surgery were SM 
(38.4%) and SR (47.6%). The majority (86.8%) of revisions 
for SM occur within the first 6 months, while most (87.9%) 
revisions for SR occur after month 6. The 4-year probability 
of revision due to SM was 1.0%; the 4-year probability of 
revision due to SR was 1.94%. Revision rates for both con­
ditions improved over time (P,0.0001 for SM, P=0.0118 

</page>
<page number='5'>
Medical Devices: Evidence and Research 2015:8
submit your manuscript | www.dovepress.com
Dovepress 
Dovepress
488
Cher et al
for SR). In the more recent time period (2012–present, 
Figure 2), the cumulative 2-year risk of revision was ∼2.5%; 
0.9% for SM and 1.07% for SR.
Kaplan–Meier analysis was used to evaluate other factors 
potentially predictive of the likelihood of revision. Revision 
rates were slightly higher with young age (P=0.024) but did 
not vary by sex (P=0.193). The number of bilateral revision 
cases (n=10) was too small to determine a meaningful effect. 
Revision rate varied by index surgeon (P,0.0001). Taking 
into account the numbers of index surgeries and follow-up 
time, each surgeon’s ratio of observed to expected revisions 
was calculated, along with confidence intervals and the ratio 
of observed/expected. In all, 22 surgeons (3.2% of all sur­
geons) had observed/expected ratios that were statistically 
elevated (ie, the lower confidence limit of the exact Poisson 
confidence interval exceeded 1); 110 revision surgeries were 
associated with these 22 surgeons, constituting 34.8% of all 
Table 2 Characteristics of revisions (n=315); cases that could 
not be linked are excluded
Characteristic
N (%)
Sex
  Female
  Male
  Unknown

187 (59.2)
69 (21.9)
59 (18.7)
Age
  ,25
  25–35
  35–45
  45–55
  55–65
  .65
  Unknown

5 (1.6)
22 (7.0)
51 (16.2)
61 (19.4)
51 (16.2)
45 (14.3)
80 (25.4)
Year of index surgery
  2009
  2010
  2011
  2012
  2013
  2014

4 (1.3)
19 (6.0)
63 (20.0)
95 (30.2)
95 (30.2)
39 (12.4)
Reason for revision
  Symptomatic malposition
  Recurrence of symptoms
  Never improved
  Fracture of ilium
  Early revision for asymptomatic 
implant malposition

121 (38.4)
150 (47.6)
29 (9.2)
3 (1.0)
12 (3.8)
Months to revision
  Same day
  ,1
  1–3
  3–6
  6–12
  12–24
  24–36
  .36

10 (3.2)
67 (21.3)
26 (8.3)
31 (9.8)
66 (21.0)
82 (26.0)
24 (97.6)
9 (2.9)
Note: *Data cut-off at July 15, 2014.
Table 1 Information from commercial database (n=11,388)
Characteristic
N (%)
Sex
  Female
  Male
  Unknown

6,709 (58.9)
2,961 (26.0)
1,718 (15.1)
Age
  ,25
  25–35
  35–45
  45–55
  55–65
  .65
  Unknown

102 (0.9)
588 (5.2)
1,565 (13.7)
2,399 (21.1)
2,056 (18.1)
2,512 (22.1)
2,166 (19.0)
Year of surgery
  2009
  2010
  2011
  2012
  2013
  2014*

31 (0.3)
256 (2.2)
1,254 (11.0)
3,163 (27.8)
4,256 (37.4)
2,428 (21.3)
Unilateral
Bilateral
10,956 (96.2)
432 (3.8)
Number of implants
  Unavailable
  Unilateral surgeries
    2
    3
    4
    5
  Bilateral surgeries
    4
    5
    6
    7
    8
All

313 (2.7)

701
9,545
409
1

67
15
322
7
8
11,388
Note: *Data cut-off at July 15, 2014.
revisions, yet these surgeons accounted for only 5.4% of 
index cases performed.
For the 25 surgeons who had performed more than 
100 cases, cases were divided by case number into cases 1–20, 
21–50, 51–100, and .100. The 12-month all-cause revision 
rates progressively decreased (1.6%, 1.1%, 0.8%, and 0.74%, 
respectively, P=0.0041). Of the 138 surgeons who had per­
formed at least 20 cases, the 12-month revision rates during 
the first 20 cases progressively improved by year the first case 
was performed (6.0%, 2.5%, 1.5%, 1.8%, and 0.7% from 2009 
to 2013, respectively, P=0.0952). Twelve-month revision rates 
for cases performed in 2014 could not be ­calculated, as only 
a single surgeon had performed 20 cases.
A review of the published literature on the iFuse Implant 
System showed a revision rate ranging from 0.7% to 9.1% over 
a period of 6 to 40 months.11,12,21,22 In an ongoing prospective 

</page>
<page number='6'>
Medical Devices: Evidence and Research 2015:8
submit your manuscript | www.dovepress.com
Dovepress 
Dovepress
489
Implant survivorship analysis of iFuse Implant System®
0.10
0.08
Cumulative probability of revision
0.06
0.04
0.02
0.00
0
6
12
18
24
30
2014
2013
2012
2011
2010
36
42
48
54
60
66
72
Months since index surgery
Figure 1 Cumulative probability of all-cause revision after sacroiliac joint fusion using iFuse Implant System® by year of placement.
Note: Shaded regions represent 95% confidence intervals.
0.02
Cumulative probability of revision
0.01
0.00
0
6
12
Recurrence
Symptomatic malposition
All causes
Months after index surgery
18
24
Figure 2 Cumulative probability of revision after sacroiliac joint fusion using iFuse Implant System® for symptomatic malposition, symptomatic recurrence, and all causes for 
surgeries taking place between 2012 and 2014.
trial of iFuse Implant System (Sacroiliac Joint Fusion With 
iFuse Implant System, n=172, NCT 01640353), the cumula­
tive 18-month revision rate was 2.8%.16 In another ongoing 
prospective randomized controlled trial (Investigation of 
­Sacroiliac Fusion Treatment, n=148, NCT01681004), one 
of 102 (0.98%) subjects assigned to SI joint fusion using the 
iFuse implant has undergone revision of the index side.17
Discussion
Three key observations determine the value of surgical proce­
dures with permanent implants: effectiveness (ie, the ability 
of the procedure/device to improve the target ­condition), 
perioperative safety, and long-term safety. A key feature 
of long-term safety is the need for a revision surgery, an 
outcome of importance to the patient, surgeon, and payor. 
Revision rate is a well-accepted endpoint in much of the 
orthopedic literature.
Our analysis of revision rates associated with the use of 
iFuse Implant System showed several key findings. First, 
the revision rate calculated in the nonclinical trial (ie, com­
mercial) setting was similar to that observed in two ongoing 
prospective trials. The observed rate fell within the values 
reported in the published literature (which constitutes a sub­
sample of the entire cohort we report herein).11,13–15,21,23

</page>
<page number='7'>
Medical Devices: Evidence and Research 2015:8
submit your manuscript | www.dovepress.com
Dovepress 
Dovepress
490
Cher et al
Second, the 4-year revision rate of 3.6% is intermediate 
when compared with rates reported after other orthopedic 
procedures. For example, in total hip replacement, a mature 
technology and surgical procedure, recent figures from Europe 
indicate 4-year revision rates of ,2%;24,25 in the US, revision 
rates might be higher (4% at 4 years).26 In a retrospective 
cohort analysis of Medicare claims, 4-year revision rates after 
lumbar stenosis surgery (decompression or arthrodesis) for 
lumbar stenosis were 10.6% and 17.2% for patients without 
and with prior surgery, respectively.27 The 4-year revision rate 
was 10.7% after simple lumbar arthrodesis and 13.5% after 
complex lumbar arthrodesis; device-related complications 
were reported for 29.2% of the reoperations. An analysis of 
discharge registry data from nonfederal acute care hospitals 
in Washington state revealed 4-year cumulative revision rates 
of 10%–20% for surgery related to a primary diagnosis of 
herniated disc, degenerative disc disease, or spondylolisthe­
sis.28 The 4-year revision rate for lumbar discectomy, a widely 
accepted surgical treatment for disc herniation, was 13.8%; 
this reoperation rate varied by surgeon.29 The 5-year revision 
rate reported from the CHARITÉ lumbar disc replacement 
investigational device exemption (IDE) trial was 7.7%.30 
Using the US Nationwide Inpatient Sample, the 2-year revi­
sion burden for lumbar disc replacement (ie, the proportion of 
disc replacement procedures that are revisions) was estimated 
at 11.2%.31 A European study of revisions after lumbar disc 
replacement noted a 10.5% revision rate of the target area at 
a mean of 8 years after initial surgery (not counting surgery 
for adjacent segment degeneration).32 In comparison to other 
commonly performed spine surgeries, the revision rate of 
3.6% after MIS SI joint fusion using the iFuse Implant System 
appears relatively low.
Revisions after MIS SI joint fusion fell predominantly 
into two categories: SM or SR. SM typically manifests as 
new pain down the ipsilateral leg as a result of impingement 
of the device on local spinal nerve root(s). Not surprisingly, 
revisions for SM typically occur within the first 30 days after 
device placement. In fact, 24% of all revisions occurred 
in the first 30 days, primarily due to SM. SR may develop 
when implant placement does not provide sufficient long-
term stabilization of the joint. Evaluations of these patients 
commonly show that one or more of the implants did not 
adequately cross the joint and engage the sacrum. Thus, 
revisions for SR generally occur after longer time periods 
compared to SM. In all, 63% of all revisions occurred within 
the first year after implant placement. Overall, however, the 
implant revision rate was fairly low. Additional potential 
explanations for late revisions include implant loosening or 
failure to achieve bony fusion. These details are not routinely 
collected during standard postmarket surveillance and their 
occurrence in clinical trials has been uncommon.
Failures of surgical procedures involving implants can fall 
into three broad categories: surgeon factors, device factors, 
or patient factors. In our analysis, no revision was attributed 
to implant failure (ie, breakage). During the time period 
under study, there were neither major changes to the physical 
characteristics of the iFuse device nor improvements in the 
delivery system; thus, these factors are unlikely to contribute 
to differential risks of implant revision. Our analysis showed 
that older patients were somewhat less likely to undergo 
revision, possibly because of increased overall surgical risks 
in older populations or competing mortality. Revision rate 
did not vary by sex.
Surgeon experience is often a factor in the risk of adverse 
events, including revision surgery.33 In addition, the learn­
ing curve for most minimally invasive spinal procedures 
has been shown to be relatively long.34–36 Our analysis sug­
gests that surgeon experience may play a role with the iFuse 
implant procedure. Overall, revision rates after MIS SI joint 
fusion using the iFuse device decreased markedly over time. 
Revisions for SM, typically resulting from incorrect device 
placement, also diminished over time. For surgeons who had 
performed .100 cases, 12-month revision rates were lower 
for the 100th + case (0.74%) versus the first 20 cases (1.6%). 
In addition, in all surgeons’ first 20 cases, 12-month revision 
rates progressively decreased over time, with the lowest rates 
during 2013. These findings suggest improvements in surgeon 
technique with increased experience and perhaps improved 
physician training over time. In our analysis, a small number 
of surgeons (2.6% of all surgeons) accounted for 34% of all 
revisions, suggesting that surgeon proficiency may be a factor 
in risk of revision. Variation in surgeon expertise may play a 
role in other procedures.28,33
The strengths of this study are three-fold. First, the 
number of index surgeries performed is captured with high 
fidelity in our inventory database as both implants and 
instruments are ordered and purchased directly through the 
company. Second, a company representative is nearly always 
in attendance for both index procedures and revisions. Third, 
although revision is uncommon, because it is an important 
clinical outcome, and because specialized iFuse instrumenta­
tion is typically used during a revision surgery, the occurrence 
of a revision surgery is likely to be reported to the company 
with relatively high fidelity.
Our investigation has several limitations. Patient charac­
teristics, other than age and sex, were unavailable, limiting 

</page>
<page number='8'>
Medical Devices: Evidence and Research 2015:8
submit your manuscript | www.dovepress.com
Dovepress 
Dovepress
491
Implant survivorship analysis of iFuse Implant System®
our ability to determine whether any other patient factors (eg, 
body mass index, sacral anatomy, comorbidities) may affect 
the risk of revision. Although only a small number of known 
revision surgeries could not be linked to index surgeries, the 
analysis may not accurately account for all revision surgeries. 
It is possible that a surgeon not familiar with or trained in 
the use of the iFuse Implant System performed a revision 
surgery but failed to report it to the company. It is also pos­
sible that revisions took place that involved procedures (eg, 
bone grafting, placement of alternative devices) that were not 
reported to or detected by the company; this could result in 
an underreporting of revision rates. In five cases (1.6% of all 
revision cases), we were aware that a revision surgery took 
place but unable to link the revision to an index surgery; this 
results in a small underestimation of the cumulative prob­
ability of revision. Our analysis is based on data from year 
2009 through 2014. In the earlier time period, the number of 
index surgeries was comparatively small. The 4-year revision 
rates are therefore based on a follow-up of a relatively small 
number of patients. However, since revision rates have fallen 
over time, the reported 3.5% rate is conservative; the actual 
current 4-year rate is likely to be lower.
Our analysis does not include death due to other causes, 
which would result in censoring of observations. Whether 
such censoring would result in increases or decreases in the 
calculated revision rate is not known.
Finally, some patients who have inadequate pain relief 
after SI joint fusion may undergo treatment for another 
condition. Our analysis does not capture these patients as 
the procedure provided is not an SI joint revision surgery. 
Clinical failure rates are best estimated from ongoing pro­
spective studies of SI joint fusion.
Despite these limitations, our investigation demonstrates 
the value of postmarket surveillance via monitoring manu­
facturer complaints. Moreover, because index surgeries and 
revisions are likely captured with high fidelity, we believe 
our analysis gives a fair representation of revision rates after 
MIS SI joint fusion using the iFuse Implant System.
Conclusion
The cumulative rate of revision surgery after SI joint fusion 
using the iFuse Implant System was 3.6% at 4 years. This 
compares favorably with revision rates for other common 
orthopedic procedures, being somewhat higher than a mature 
orthopedic technology (total hip replacement) but less than 
commonly performed lumbar spine surgeries. The revision 
rate improved annually from 2009, possibly related to a 
surgeon learning curve or improved training.
Author contributions
All authors contributed toward data analysis, drafting and 
revising the paper and agree to be accountable for all aspects 
of the work.
Disclosure
All authors are SI-BONE employees. The authors report no 
other conflicts of interest in this work.
References
	 1.	 Quality System Regulation; Complaint Files. Code of Federal Regula­
tions, Title 21, Part 820. Available from: ,http://www.accessdata.
fda.gov/scripts/cdrh/cfdocs/cfCFR/CFRSearch.cfm?FR=820.198.. 
Accessed July 1, 2014.
	 2.	 Medical Device Reporting. Code of Federal Regulations, Title 21, 
Part 803. Available from: ,http://www.accessdata.fda.gov/scripts/
cdrh/cfdocs/cfCFR/CFRSearch.cfm?CFRPart=803.. Accessed July 1, 
2014.
	 3.	 Leopold SS. Editorial: when ‘safe and effective’ becomes dangerous. 
Clin Orthop. 2014;472:1999–2001.
	 4.	 Urban RM, Jacobs JJ, Tomlinson MJ, Gavrilovic J, Black J, Peoc’h M. 
Dissemination of wear particles to the liver, spleen, and abdominal 
lymph nodes of patients with hip or knee replacement. J Bone Joint 
Surg Am. 2000;82:457–476.
	 5.	 Rice NT, Hu Y, Slaughter JC, Ward RM. Pelvic mesh complications 
in women before and after the 2011 FDA public health notification. 
Female Pelvic Med Reconstr Surg. 2013;19:333–338.
	 6.	 Koski ME, Rovner ES. Implications of the FDA statement on transvagi­
nal placement of mesh: the aftermath. Curr Urol Rep. 2014;15:380.
	 7.	 Stephenson J. FDA warns against procedure used in removing fibroids. 
JAMA. 2014;311:1956.
	 8.	 Brown SL, Bright RA, Tavris DR. Medical Device Epidemiology and 
Surveillance. Chichester: John Wiley & Sons; 2007.
	 9.	 Buchowski JM, Kebaish KM, Sinkov V, Cohen DB, Sieber AN, 
Kostuik JP. Functional and radiographic outcome of sacroiliac arthrod­
esis for the disorders of the sacroiliac joint. Spine J. 2005;5:520–528.
	10.	 Heiney J, Capobianco R, Cher D. Systematic review of minimally 
invasive sacroiliac joint fusion using a lateral transarticular approach. 
Int J Spine Surg. 2015;9:40.
	11.	 Sachs D, Capobianco R, Cher D, et al. One-year outcomes after minimally 
invasive sacroiliac joint fusion with a series of triangular implants: a multi­
center, patient-level analysis. Med Devices Evid Res. 2014;7: 299–304.
	12.	 Rudolf L. Sacroiliac Joint Arthrodesis-MIS technique with titanium 
implants: report of the first 50 patients and outcomes. Open Orthop J. 
2012;6:495–502.
	13.	 Vanaclocha V, Verdu-Lopez F, Sanchez-Pardo M, et al. Minimally 
invasive sacroiliac joint arthrodesis: experience in a prospective series 
with 24 patients. J Spine. 2014;3:7.
	14.	 Rudolf L, Capobianco R. Five-year clinical and radiographic outcomes 
after minimally invasive sacroiliac joint fusion using triangular implants. 
Open Orthop J. 2014;8:375–383.
	15.	 Gaetani P, Miotti D, Risso A. Percutaneous arthrodesis of sacro-iliac 
joint: a pilot study. J Neurosurg Sci. 2013;57:297–301.
	16.	 Duhon BS, Cher DJ, Wine K, Kovalsky D, Lockstadt H. Triangular 
titanium implants for minimally invasive sacroiliac joint fusion: 
a prospective study. Glob Spine J. Epub 2015 Aug 11.
	17.	 Polly DW, Cher DJ, Wine KD, et al. Randomized controlled trial of 
minimally invasive sacroiliac joint fusion using triangular titanium 
implants vs nonsurgical management for sacroiliac joint dysfunction: 
12-month outcomes. Neurosurgery. 2015;77:674–691.
	18.	 Ahn J, Iqbal A, Manning BT, et  al. Minimally invasive lumbar 
decompression – the surgical learning curve. Spine J. Epub 2015 
Aug 11.

</page>
<page number='9'>
Medical Devices: Evidence and Research
Publish your work in this journal
Submit your manuscript here: http://www.dovepress.com/medical-devices-evidence-and-research-journal
Medical Devices: Evidence and Research is an international, peer-
reviewed, open access journal that focuses on the evidence, technology, 
research, and expert opinion supporting the use and application of 
medical devices in the diagnosis, treatment and management of clini­
cal conditions and physiological processes. The identification of novel 
devices and optimal use of existing devices which will lead to improved 
clinical outcomes and more effective patient management and safety is 
a key feature. The manuscript management system is completely online 
and includes a quick and fair peer-review system. Visit http://www.
dovepress.com/testimonials.php to read real quotes from authors.
Medical Devices: Evidence and Research 2015:8
submit your manuscript | www.dovepress.com
Dovepress 
Dovepress
Dovepress
492
Cher et al
	19.	 Garwood F. (i) Fiducial limits for the Poisson distribution. Biometrika. 
1936;28:437–442.
	20.	 R Core Team (2013). R: A Language and Environment for Statistical 
Computing. Available from: ,http://www.R-project.org/.. Accessed 
September 1, 2014.
	21.	 Smith AG, Capobianco R, Cher D, et al. Open versus minimally inva­
sive sacroiliac joint fusion: a multi-center comparison of perioperative 
measures and clinical outcomes. Ann Surg Innov Res. 2013;7:14.
	22.	 Ledonio CG, Polly DW, Swiontkowski MF. Minimally invasive versus 
open sacroiliac joint fusion: are they similarly safe and effective? Clin 
Orthop Relat Res. 2014;472:1831–1838.
	23.	 Duhon B, Cher DJ, Wine KD, Lockstadt H, Kovalsky D, Soo CL. Safety 
and 6-month effectiveness of minimally invasive sacroiliac joint fusion: 
a prospective study. Med Devices Evid Res. 2013;6:219–229.
	24.	 Garellick G, Kärrholm J, Rogmark C, Herberts P. Swedish hip arthro­
plasty register. Annual Report; 2010. Available from: ,http://linkmedi
cal.ru/data/AnnualReport-2010-eng.pdf.. Accesssed July 5, 2015.
	25.	 Clarke A, Pulikottil-Jacob R, Grove A, et al. Total hip replacement and 
surface replacement for the treatment of pain and disability resulting 
from end-stage arthritis of the hip (review of technology appraisal 
guidance 2 and 44): systematic review and economic evaluation. Health 
Technol Assess. 2015;19:1–668.
	26.	 Kurtz SM, Ong KL, Schmier J, et al. Future clinical and economic 
impact of revision total hip and knee arthroplasty. J Bone Joint Surg 
Am. 2007;89 Suppl 3:144–151.
	27.	 Deyo RA, Martin BI, Kreuter W, Jarvik JG, Angier H, Mirza SK. 
Revision surgery following operations for lumbar stenosis. J Bone Joint 
Surg Am. 2011;93:1979–1986.
	28.	 Martin BI, Mirza SK, Comstock BA, Gray DT, Kreuter W, Deyo RA. 
Reoperation rates following lumbar spine surgery and the influence of 
spinal fusion procedures. Spine. 2007;32:382–387.
	29.	 Martin BI, Mirza SK, Flum DR, et al. Repeat surgery after lumbar 
decompression for herniated disc: the quality implications of hospital 
and surgeon variation. Spine J. 2012;12:89–97.
	30.	 Guyer RD, McAfee PC, Banco RJ, et al. Prospective, randomized, mul­
ticenter Food and Drug Administration investigational device exemption 
study of lumbar total disc replacement with the CHARITE artificial disc 
versus lumbar fusion: five-year follow-up. Spine J. 2009;9:374–386.
	31.	 Kurtz SM, Lau E, Ianuzzi A, et al. National revision burden for lumbar 
total disc replacement in the United States: epidemiologic and economic 
perspectives. Spine. 2010;35:690–696.
	32.	 Siepe CJ, Heider F, Wiechert K, Hitzl W, Ishak B, Mayer MH. Mid- 
to long-term results of total lumbar disc replacement: a prospective 
analysis with 5- to 10-year follow-up. Spine J. 2014;14:1417–1431.
	33.	 Labek G, Thaler M, Janda W, Agreiter M, Stöckl B. Revision rates after 
total joint replacement: cumulative results from worldwide joint register 
datasets. J Bone Joint Surg Br. 2011;93:293–297.
	34.	 Lee KH, Yeo W, Soeharno H, Yue WM. Learning curve of a complex 
surgical technique: minimally invasive transforaminal lumbar interbody 
fusion (MIS TLIF). J Spinal Disord Tech. 2014;27:E234–E240.
	35.	 Jhala A, Mistry M. Endoscopic lumbar discectomy: experience of first 
100 cases. Indian J Orthop. 2010;44:184–190.
	36.	 Sclafani JA, Kim CW. Complications associated with the initial learning 
curve of minimally invasive spine surgery: a systematic review. Clin 
Orthop. 2014;472:1711–1717.

</page>
</source_document>


--- END SOURCE DOCUMENTS ---
