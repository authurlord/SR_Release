# BIRD-Dev / thrombosis_prediction — Schema and business semantics

The saved catalogue for this database contains 3 tables, 64 physical columns, 2 relationships and 3 source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.

## Examination

Stores laboratory examination results and diagnoses for patients, including antiphospholipid antibody tests and thrombosis indicators.

Recovered table names: examination / Exam / Lab Test / Blood Test / Test Results
SQL table aliases: E, T1, T2, T3, e

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Examination.XCL_001 | id / identifier / Examination ID / Exam ID / Record ID / Test ID | integer | schema / Examination |
| Examination.XCL_002 | examination date / Exam Date / Test Date / Date of Exam / Date of Test | date | schema / Examination |
| Examination.XCL_003 | a cl ig g / aCL IgG / Anticardiolipin IgG / IgG anticardiolipin / Cardiolipin IgG | real | schema / Examination |
| Examination.XCL_004 | a cl ig m / aCL IgM / Anticardiolipin IgM / IgM anticardiolipin / Cardiolipin IgM | real | schema / Examination |
| Examination.XCL_005 | ana / Antinuclear Antibody / Antinuclear Antibody Titer / ANA titer | integer | schema / Examination |
| Examination.XCL_006 | ana pattern / Antinuclear Antibody Pattern / ANA staining pattern / Immunofluorescence pattern | text | schema / Examination |
| Examination.XCL_007 | a cl ig a / aCL IgA / Anticardiolipin IgA / IgA anticardiolipin / Cardiolipin IgA | integer | schema / Examination |
| Examination.XCL_008 | diagnosis / Diagnoses / Medical Diagnosis / Condition / Disease | text | schema / Examination |
| Examination.XCL_009 | kct / Kaolin Clotting Time | text | schema / Examination |
| Examination.XCL_010 | rvvt / Russell Viper Venom Time | text | schema / Examination |
| Examination.XCL_011 | lac / Lupus Anticoagulant / Lupus anticoagulant test | text | schema / Examination |
| Examination.XCL_012 | symptoms / Symptom / Clinical Symptoms / Presenting Symptoms | text | schema / Examination |
| Examination.XCL_013 | thrombosis / Thrombosis Indicator / Thrombosis Score / Thrombosis Count | integer | schema / Examination |

## Patient

Stores demographic and clinical information for patients in a thrombosis prediction context.

Recovered table names: patient / patients / patient records / patient demographics
SQL table aliases: P, T1, p, p2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Patient.XCL_058 | id / identifier / patient ID / patient identifier / patient number / unique patient ID | integer | schema / Patient |
| Patient.XCL_059 | sex / gender / patient gender / biological sex | text | schema / Patient |
| Patient.XCL_060 | birthday / date of birth / birth date / DOB / patient birth date | date | schema / Patient |
| Patient.XCL_061 | description / description date / record date / entry date / date of description | date | schema / Patient |
| Patient.XCL_062 | first date / initial date / first visit date / first encounter date | date | schema / Patient |
| Patient.XCL_063 | admission / admission status / admission indicator / admission flag / admission code | text | schema / Patient |
| Patient.XCL_064 | diagnosis / diagnosis code / diagnosis text / medical diagnosis | text | schema / Patient |

## Laboratory

Stores laboratory test results for patients, including blood chemistry, hematology, coagulation, immunology, and serology tests.

Recovered table names: laboratory / Lab / Labs / Laboratory Tests / Lab Results / Lab Values
SQL table aliases: L, T1, T2, l, l2

| Physical | Recovered names | Type | Sources |
|---|---|---|---|
| Laboratory.XCL_014 | id / identifier / Patient ID / Patient Identifier / Lab Record ID / Lab ID | integer | schema / Laboratory |
| Laboratory.XCL_015 | date / Test Date / Lab Date / Collection Date / Result Date | date | schema / Laboratory |
| Laboratory.XCL_016 | got / AST / Aspartate Aminotransferase / SGOT / Serum Glutamic Oxaloacetic Transaminase | integer | schema / Laboratory |
| Laboratory.XCL_017 | gpt / ALT / Alanine Aminotransferase / SGPT / Serum Glutamic Pyruvic Transaminase | integer | schema / Laboratory |
| Laboratory.XCL_018 | ldh / Lactate Dehydrogenase / Lactic Dehydrogenase / LD | integer | schema / Laboratory |
| Laboratory.XCL_019 | alp / Alkaline Phosphatase / Alk Phos / ALPase | integer | schema / Laboratory |
| Laboratory.XCL_020 | tp / Total Protein / Serum Total Protein | real | schema / Laboratory |
| Laboratory.XCL_021 | alb / Albumin / Serum Albumin | real | schema / Laboratory |
| Laboratory.XCL_022 | ua / Uric Acid / Urate | real | schema / Laboratory |
| Laboratory.XCL_023 | un / Urea Nitrogen / Blood Urea Nitrogen / BUN | integer | schema / Laboratory |
| Laboratory.XCL_024 | cre / Creatinine / Serum Creatinine | real | schema / Laboratory |
| Laboratory.XCL_025 | t bil / Total Bilirubin / Bilirubin Total / TBIL / T-Bil | real | schema / Laboratory |
| Laboratory.XCL_026 | t cho / Total Cholesterol / Cholesterol Total / TCHO / T-Chol | integer | schema / Laboratory |
| Laboratory.XCL_027 | tg / Triglycerides / Triglyceride | integer | schema / Laboratory |
| Laboratory.XCL_028 | cpk / Creatine Phosphokinase / Creatine Kinase / CK | integer | schema / Laboratory |
| Laboratory.XCL_029 | glu / Glucose / Blood Sugar | integer | schema / Laboratory |
| Laboratory.XCL_030 | wbc / White Blood Cell Count / White Cell Count / Leukocyte Count | real | schema / Laboratory |
| Laboratory.XCL_031 | rbc / Red Blood Cell Count / Red Cell Count / Erythrocyte Count | real | schema / Laboratory |
| Laboratory.XCL_032 | hgb / Hemoglobin / Hb | real | schema / Laboratory |
| Laboratory.XCL_033 | hct / Hematocrit / Packed Cell Volume / PCV | real | schema / Laboratory |
| Laboratory.XCL_034 | plt / Platelet Count / Thrombocyte Count | integer | schema / Laboratory |
| Laboratory.XCL_035 | pt / Prothrombin Time / Pro Time | real | schema / Laboratory |
| Laboratory.XCL_036 | aptt / Activated Partial Thromboplastin Time / PTT | integer | schema / Laboratory |
| Laboratory.XCL_037 | fg / Fibrinogen / Factor I | real | schema / Laboratory |
| Laboratory.XCL_038 | pic / Plasminogen Activator Inhibitor Complex / PAI-1 Complex | integer | schema / Laboratory |
| Laboratory.XCL_039 | tat / Thrombin-Antithrombin Complex / TAT Complex | integer | schema / Laboratory |
| Laboratory.XCL_040 | tat2 / Thrombin-Antithrombin Complex 2 / TAT II | integer | schema / Laboratory |
| Laboratory.XCL_041 | u pro / Urine Protein / Proteinuria / U-Protein / U-PRO | text | schema / Laboratory |
| Laboratory.XCL_042 | igg / Immunoglobulin G / Gamma Globulin | integer | schema / Laboratory |
| Laboratory.XCL_043 | iga / Immunoglobulin A / Alpha Globulin | integer | schema / Laboratory |
| Laboratory.XCL_044 | igm / Immunoglobulin M / Macroglobulin | integer | schema / Laboratory |
| Laboratory.XCL_045 | crp / C-Reactive Protein / hs-CRP | text | schema / Laboratory |
| Laboratory.XCL_046 | ra / Rheumatoid Arthritis Factor / RA Factor / RA Test | text | schema / Laboratory |
| Laboratory.XCL_047 | rf / Rheumatoid Factor / Rheumatoid Factor Test | text | schema / Laboratory |
| Laboratory.XCL_048 | c3 / Complement C3 / Complement Component 3 | integer | schema / Laboratory |
| Laboratory.XCL_049 | c4 / Complement C4 / Complement Component 4 | integer | schema / Laboratory |
| Laboratory.XCL_050 | rnp / Ribonucleoprotein Antibody / Anti-RNP / RNP Antibody | text | schema / Laboratory |
| Laboratory.XCL_051 | sm / Smith Antibody / Anti-Sm / Sm Antibody | text | schema / Laboratory |
| Laboratory.XCL_052 | sc170 / Scl-70 Antibody / Anti-Scl-70 / Topoisomerase I Antibody | text | schema / Laboratory |
| Laboratory.XCL_053 | ssa / Anti-SSA Antibody / Ro Antibody / Sjogren's Syndrome A Antibody | text | schema / Laboratory |
| Laboratory.XCL_054 | ssb / Anti-SSB Antibody / La Antibody / Sjogren's Syndrome B Antibody | text | schema / Laboratory |
| Laboratory.XCL_055 | centromea / Centromere Antibody / Anti-Centromere / Centromere B Antibody | text | schema / Laboratory |
| Laboratory.XCL_056 | dna / Anti-dsDNA Antibody / Double-Stranded DNA Antibody / DNA Antibody | text | schema / Laboratory |
| Laboratory.XCL_057 | dna ii / Anti-dsDNA Antibody II / DNA Antibody II / dsDNA II | integer | schema / Laboratory |

## Relationships and join evidence

- Examination.XCL_001 ↔ Patient.XCL_058; declared_or_materialized_relationship
- Laboratory.XCL_014 ↔ Patient.XCL_058; declared_or_materialized_relationship

## Business definitions, population and grain


## Incremental maintenance events

