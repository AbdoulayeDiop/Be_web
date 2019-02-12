conf = Import('../data/config.py')
chemin = conf.chemin()


def index():
    if "nom" in COOKIE:
        cv = '''<!DOCTYPE html>
                <html>
                <head>
                <title>Aymeric LE CALVEZ - CV</title>
                
                <meta name="viewport" content="width=device-width"/>
                <meta name="description" content="The Curriculum Vitae of Aymeric Le Calvez."/>
                <meta charset="UTF-8"> 
                
                <link type="text/css" rel="stylesheet" href="'''+chemin+'''/assets/css/cv_aymeric.css" />
                <link href='http://fonts.googleapis.com/css?family=Rokkitt:400,700|Lato:400,300' rel='stylesheet' type='text/css'>
                
                <!--[if lt IE 9]>
                <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
                <![endif]-->
                </head>
                <body id="top">
                <div id="cv" class="instaFade">
                    <div class="mainDetails">
                        <div id="headshot" class="quickFade">
                            <img src="'''+chemin+'''/cv_webmaster/photo_aymeric.jpg" alt="Alan Smith" />
                        </div>
                        
                        <div id="name">
                            <h1 class="quickFade delayTwo">Aymeric Le Calvez</h1>
                            <h2 class="quickFade delayThree">Etudiant ingénieur à l'ENAC Toulouse</h2>
                        </div>
                        
                        <div id="contactDetails" class="quickFade delayFour">
                            <ul>
                                <li><a href="mailto:aymeric.lecalvez@gmail.com" target="_blank">aymeric.lecalvez@gmail.com</a></li>
                                <li>+33682620053</li>
                                <li><a href=https://www.linkedin.com/in/aymeric-le-calvez-736b20152/ target="_blank">Linkedin Aymeric Le Calvez</a></li>
                            </ul>
                        </div>
                        <div class="clear"></div>
                    </div>
                    
                    <div id="mainArea" class="quickFade delayFive">
                            <section>
                            <div class="sectionTitle">
                                <h1>Education</h1>
                            </div>
                            
                            <div class="sectionContent">
                                <article>
                                    <h2>Eleve ingénieur civil à l'Ecole Nationale de l'Aviation Civile</h2>
                                    <p class="subDetails">2017 - 2018</p>
                                    <p>TOULOUSE</p>
                                </article>
                                
                                <article>
                                    <h2>Classes préparatoires PTSI/PT*</h2>
                                    <p class="subDetails">2015 - 2017</p>
                                    <p>Lycée La Martinière Monplaisir LYON</p>
                                </article>
                                
                                <article>
                                    <h2>Bacalauréat scientifique (spécialité SI_ option maths)</h2>
                                    <p class="subDetails">2012 - 2015</p>
                                    <p>Lycée Parc Chabrières OULLINS</p>
                                </article>
                            </div>
                            <div class="clear"></div>
                        </section>
                    
                    <section>
                            <div class="sectionTitle">
                                <h1>Experience professionnelle</h1>
                            </div>
                            
                            <div class="sectionContent">
                                <article>
                                    <h2>Eté 2015</h2>
                                    <p>CDD dans une association de parents d’élèves pour l’inscription des nouveaux adhérents et le Prêt des Manuels Scolaires (PMS)</p>
                                    <p>Juillet : Récupération, tri, inventaire des livres</p>
                                    <p>Fin août : Préparation des collections et distribution de rentrée</p>
                                </article>
                                
                                <article>
                                    <h2>Années 2013 et 2014 </h2>
                                    <p>Bénévole dans cette même association pour le PMS</p>
                                </article>
                                
                                <article>
                                    <h2>Février 2012</h2>
                                    <p>Stage de troisième - Pôle Technique de Lyon, Société Total. Découverte de l’entreprise et de ses différents métiers</p>
                                </article>
                            </div>
                            <div class="clear"></div>
                        </section>
                        
                        <section>
                            <div class="sectionTitle">
                                <h1>Compétences</h1>
                            </div>
                            
                            <div class="sectionContent">
                                <ul class="keySkills">
                                    <li>Microsoft Office</li>
                                    <li>Solidworks</li>
                                    <li>Python</li>
                                    <li>SQL</li>
                                    <li>HTML</li>
                                </ul>
                            </div>
                            <div class="clear"></div>
                        </section>
                        
                        <section>
                            <article>
                                <div class="sectionTitle">
                                    <h1>Centres d'intérêt</h1>
                                </div>
                                
                                <div class="sectionContent">
                                    <article>
                                        <p>Membre du pôle communication aux EAG, le tournoi sportif européen organisé par l'ENAC : prise de contact avec les universités espagnoles, inscription des participants et publications sur les réseaux sociaux</p>
                                    </article>
                                    <ul class="keySkills">
                                        <li>Volley (2 ans)</li>
                                        <li>Randonnée</li>
                                        <li>VTT</li>
                                        <li>Guitare Basse</li>
                                        <li>Lecture</li>
                                    </ul>
                                </div>
                            </article>
                            <div class="clear"></div>
                        </section>
                        
                    </div>
                </div>
                <script type="text/javascript">
                var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
                document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
                </script>
                <script type="text/javascript">
                var pageTracker = _gat._getTracker("UA-3753241-1");
                pageTracker._initData();
                pageTracker._trackPageview();
                </script>
                </body>
                </html>'''
        return cv
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')


