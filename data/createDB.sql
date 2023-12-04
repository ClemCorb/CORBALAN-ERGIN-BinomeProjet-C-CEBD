create table Regions (
    code_region INTEGER,
    nom_region TEXT,
    constraint pk_regions primary key (code_region)
);

create table Departements (
    code_departement TEXT,
    nom_departement TEXT,
    code_region INTEGER,
    zone_climatique TEXT ,--CHECK (zone_climatique IN("H1","H2","H3"))
    constraint pk_departements primary key (code_departement)
    --constraint fk_region foreign key (code_region) references Regions(code_region)
);
create table Mesures (
    code_departement TEXT,
    date_mesure DATE,
    temperature_min_mesure FLOAT,
    temperature_max_mesure FLOAT,
    temperature_moy_mesure FLOAT,
    constraint pk_mesures primary key (code_departement, date_mesure)
   -- constraint fk_mesures foreign key (code_departement) references Departements(code_departement)
);
create table Communes(
    code_commune INTEGER,
    code_departement INTEGER,
    nom_commune TEXT,
    statut TEXT,
    altitude_moyenne INTEGER,
    population INTEGER,
    superficie INTEGER,
    code_canton INTEGER,
    code_arrondissement INTEGER,
    constraint pk_commune primary key (code_departement, code_commune),
    constraint fk_commune foreign key (code_departement) references Departements(code_departement)
);
--create table Travaux(
    --code_departement TEXT,
    --code_region TEXT,
    --id_travaux INTEGER PRIMARY KEY AUTOINCREMENT,
    --cout_total_ht FLOAT,
    --cout_induit_ht FLOAT,
    --annee INTEGER,
    --type_logement TEXT,
    --annee_construction_logement INTEGER,
    --constraint pk_travaux primary key (id_travaux),
    --constraint fk_1_travaux foreign key (code_departement) references Departements(code_departement),
  --  constraint fk_2_travaux foreign key (code_region) references Regions(code_region)
--);

create table TravauxIsolation(
    id_travaux INTEGER,
    code_departement TEXT,
    code_region INTEGER,
    cout_total_ht FLOAT,
    cout_induit_ht FLOAT,
    annee TEXT,
    type_logement TEXT,
    annee_construction_logement TEXT,
    poste TEXT CHECK (poste IN("COMBLES PERDUES","ITI","ITE","RAMPANTS","SARKING","TOITURE TERRASSE","PLANCHER BAS")),
    isolant TEXT CHECK (isolant IN ("AUTRES","LAINE VEGETALE","LAINE MINERALE","PLASTIQUES")),
    epaisseur INTEGER,
    surface FLOAT,
    constraint pk_isolations primary key (id_travaux),
    constraint fk_1_isolations foreign key (code_departement) references Departements(code_departement),
    constraint fk_2_isolations foreign key (code_region) references Regions(code_region)


);
create table TravauxChauffage (
    id_travaux INTEGER,
    code_departement TEXT,
    code_region INTEGER,
    cout_total_ht FLOAT,
    cout_induit_ht FLOAT,
    annee TEXT,
    type_logement TEXT,
    annee_construction_logement TEXT,
    energie_avant_travaux TEXT CHECK(energie_avant_travaux IN("AUTRES","BOIS","ELECTRICITE","FIOUL","GAZ")),
    energie_instalee TEEXT CHECK(energie_instalee IN("AUTRES","BOIS","ELECTRICITE","FIOUL","GAZ")),
    generateur TEXT CHECK(generateur IN("AUTRES","CHAUDIERE","INSERT","PAC","POELE","RADITEUR")),
    type_chaudiere TEXT CHECK(type_chaudiere IN("STANDART","AIR-EAU","A CONDENSATION","AUTRES","AIR-AIR","GEOTHERMIE","HPE")),
    constraint pk_chauffage primary key(id_travaux),
    constraint fk_1_chauffage foreign key (code_departement) references Departements(code_departement),
    constraint fk_2_chauffage foreign key (code_region) references Regions(code_region)

);
create table TravauxPhotovoltaique(
    id_travaux INTEGER,
    code_departement TEXT,
    code_region INTEGER,
    cout_total_ht FLOAT,
    cout_induit_ht FLOAT,
    annee TEXT,
    type_logement TEXT,
    annee_construction_logement INTEGER,
    puissance_installee INTEGER,
    type_panneaux TEXT,
    constraint pk_photovoltaique primary key (id_travaux),
    constraint fk_1_photovoltaique foreign key (code_departement) references Departements(code_departement),
    constraint fk_2_photovoltaique foreign key (code_region) references Regions(code_region)
);

--TODO Q4 Ajouter les créations des nouvelles tables