conf = Import('../data/config.py')
chemin = conf.chemin()


def index():
    if "nom" in COOKIE:
        cv = '''<!DOCTYPE html>
                <html>
                <head>
                <title>CV Abdoulaye DIOP</title>
                
                <meta name="viewport" content="width=device-width"/>
                <meta name="description" content="The Curriculum Vitae of Abdoulaye DIOP."/>
                <meta charset="UTF-8"> 
                
                <link type="text/css" rel="stylesheet" href="'''+chemin+'''/assets/css/cv_abdoulaye.css" />
                <link href='http://fonts.googleapis.com/css?family=Rokkitt:400,700|Lato:400,300' rel='stylesheet' type='text/css'>
                
                <!--[if lt IE 9]>
                <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
                <![endif]-->
                </head>
                <body id="top">
                <div id="cv" class="instaFade">
                    <div class="mainDetails">
                        <div id="headshot" class="quickFade">
                            <img src="'''+chemin+'''/cv_webmaster/photo_abdoulaye.jpg" alt="Alan Smith" />
                        </div>
                        
                        <div id="name">
                            <h1 class="quickFade delayTwo">Abdoulaye DIOP</h1>
                            <h2 class="quickFade delayThree">1ERE ANNEE ECOLE D’INGENIEUR ENAC</h2>
                        </div>
                        
                        <div id="contactDetails" class="quickFade delayFour">
                            <ul>
                                <li><a href="mailto:abdoulayediop949@yahoo.fr" target="_blank">abdoulayediop949@yahoo.fr</a></li>
                                <li>(+33)07 53 91 36 96</li>
                                <li><a href=https://www.linkedin.com/in/abdoulaye-diop-044406159/ target="_blank">Linkedin Abdoulaye DIOP</a></li>
                            </ul>
                        </div>
                        <div class="clear"></div>
                    </div>
                    
                    <div id="mainArea" class="quickFade delayFive">
                        <section>
                            <div class="sectionTitle">
                                <h1>FORMATIONS</h1>
                            </div>
                            
                            <div class="sectionContent">
                                <article>
                                    <h2>Formation « Ingenieur ENAC » 1ère année</h2>
                                    <p class="subDetails">2017 - 2018</p>
                                    <p>TOULOUSE</p>
                                </article>
                                
                                <article>
                                    <h2>CPGE – MP*</h2>
                                    <p class="subDetails">2016 - 2017</p>
                                    <p>Lycée Descartes (Tours 37000)</p>
                                </article>
                                
                                <article>
                                    <h2>CPGE – MPSI</h2>
                                    <p class="subDetails">2015 - 2016</p>
                                    <p>Lycée F. Philibert Dessaignes (Blois 41000)</p>
                                </article>
                                
                                <article>
                                    <h2>Baccalauréat Scientifique S1</h2>
                                    <p class="subDetails">2014 - 2015</p>
                                    <p>Lycée de Mbao (SENEGAL)</p>
                                </article>
                            </div>
                            <div class="clear"></div>
                        </section>
                        
                        <section>
                            <div class="sectionTitle">
                                <h1>COMPETENCES</h1>
                            </div>
                            
                            <div class="sectionContent">
                                <ul class="keySkills">
                                    <li>
                                        <h2>Anglais</h2>
                                        <ul>
                                            <li>780 au TOEIC</li>
                                        <ul>
                                    </li>
                                    <li>
                                        <h2>Informatique</h2>
                                        <ul>
                                            <li>Programmation algorithmique</li>
                                            <li>Interfaces graphiques</li>
                                            <li>Gestion de base de données</li>
                                            <li>Application Web</li>
                                        <ul>
                                    </li>
                                    <li>
                                        <h2>Logiciels et Language</h2>
                                        <ul>
                                            <li>Python (logiciel de programmation)</li>
                                            <li>QtDesigner (création d’interfaces graphiques)</li>
                                            <li>MySQL (gestion de bases de données)</li>
                                            <li>HTML, Javascript...</li>
                                            <li>Word, Excel, Powerpoint...</li>
                                        <ul>
                                    </li>
                                    <li>
                                        <h2>Relationnel</h2>
                                        <ul>
                                            <li>Accueil des étudiants et des professeurs à la bibliothèque de l’ENAC</li>
                                        <ul>
                                    </li>
                                </ul>
                            </div>
                            <div class="clear"></div>
                        </section>
                        
                        <section>
                            <div class="sectionTitle">
                                <h1>EXPERIENSE</h1>
                            </div>
                            
                            <div class="sectionContent">
                                <article>
                                    <h2>Bibliothécaire à l’ENAC (25h/mois)</h2>
                                    <p class="subDetails">Novembre/2017-Aujourd’hui</p>
                                    <p>Accueil des lecteurs, Gestion des prêt et des retours de livres</p>
                                </article>
                                
                            </div>
                            <div class="clear"></div>
                        </section>
                        
                        <section>
                            <div class="sectionTitle">
                                <h1>CENTRES D'INTERET</h1>
                            </div>
                            
                            <div class="sectionContent">
                                    <ul class="keySkills">
                                        <li>
                                            <h2>Sports</h2>
                                            <ul>
                                                <li>Football</li>
                                                <li>Basket...</li>
                                            <ul>
                                        </li>
                                        <li>
                                            <h2>Association</h2>
                                            <ul>
                                                <li>ASENAC</li>
                                            <ul>
                                        </li>
                                    </ul>
                            </div>
                            <div class="clear"></div>
                        </section>
                        
                    </div>
                </div>
                </body>
                </html>'''
        return cv
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')


