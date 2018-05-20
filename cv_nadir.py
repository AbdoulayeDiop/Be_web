conf = Import('../data/config.py')
chemin = conf.chemin()

def index():
    if "nom" in COOKIE :
        cv='''<!DOCTYPE html>
        <html lang="fr">
           <head>
                        <meta charset="utf-8">
                      <title>Nadir Ranem</title>
                       <link type="text/css" rel="stylesheet" href="'''+chemin+'''/assets/css/cv_nadir.css" />
        
           </head>
               <body>
                        <!-- Section Identité -->
                     <header>
                                      <h1>Nadir Ranem</h1>
                                   <div id="metier">Etudiant ingénieur</div>
                   </header>
                             <!-- Fin Section Identité -->
        
                      <!-- Section principale-->
                    <main>
                        <!-- Section Contact -->
                              <section id="contact">
                                   <h2>Contact</h2>
                                      <address>
                                             <ul>
                                                  <li>ENAC, Toulouse</li>
                                   <li>06 51 44 95 92</li>
                                                   <li><a href="mailto:nadirranem@yahoo.fr">nadirranem@yahoo.fr</a></li>
                                             </ul>
                                 </address>
                        </section>
        
                              <!-- Section Profil -->
                               <section id="profil" class="mainsection">
                                 <h2>Profil</h2>
                                       <p>Je suis à la recherche d'un stage ouvrier pour le mois de juillet</p>
                           </section>
        
                              <!-- Section Expériences -->
                          <section id="experiences" class="mainsection" >
                                        <h2>Expériences</h2>
        
                                      <!-- Section Expérience 1  -->
                                        <section>
                                 <div class="dates">novembre 2017 à aujourd'hui</div>
                                             <h3>Médiateur culturel</h3>
        
                                              <div class="ss-titre">ENAC <span>Toulouse</span></div>
        
                                              <div class="fonction">
                                                      <p>Assistant culturel</p>
                                                  <ul>
                                                          <li>aide à organisation des évenements</li>
                                                          <li>présentation des évenements culturels</li>
                                                  </ul>
                                         </div>
                                                <div class="competences">
                                                   <ul>
                                                             <li class="w100"><span>Bureautique</li>
                                                             <li class="w80"><span>Médiateur</span></li>
                                                             <li class="w60"><span>Manutension</span></li>
        
                                                      </ul>
                                                 </div>
        
                                  </section>
                                     <!-- FIN Section Expérience 1 -->
        
                                      <!-- Section Expérience 2 -->
                                 <section>
                                         <div class="dates">15/07/2015 à 31/07/2015</div>
                                                 <h3>Stagiaire</h3>
        
                                                      <div class="ss-titre">Ecole Polytechnique (X) <span>Palaiseau</span></div>
        
                                                      <div class="fonction">
                                                          <p> Stage de préparartion aux études supérieur </p>
                                                          <ul>
                                                                  <li>Mathématiques/physique</li>
                                                                  <li>Anglais/français</li>
                                                            </ul>
                                                 </div>
                                                        <div class="competences">
                               <ul>
                                                                   <li class="w100"><span>Sport</span></li>
                                                                   <li class="w80"><span>Math / Physique</span></li>
                                                                   <li class="w60"><span>Anglais / Français</span></li>
        
                                                              </ul>
                                                 </div>
                            </section>
                                     <!-- FIN Section Expérience 2 -->
        
                              </section>
                            <!-- Fin Section Expériences -->
        
                            <!-- Section Formation -->
                         <section id="formation" class="mainsection">
                                      <h2>Formation</h2>
        
                                      <!-- Section Formation initiale  -->
                              <section>
                                              <h3>Etudes supérieures</h3>
                                           <ul>
                                                  <li>
                                                          <p>2017 - aujourd'hui</p>
                                                          <h4>Ingénieur ENAC</h4>
                                                          <span>ENAC</span>
        
                                                      </li>
                     <li>
                                                           <p>2015 - 2017</p>
                                                            <h4>CPGE Scientifique MPSI/PSI*</h4>
                                                             <span>Lycée Marcelin Berthelot</span>
                                                   </li>
                                         </ul>
                                 </section>
        
                                      <!-- Section Formation continue  -->
              <section>
                                              <h3>Formation initiale</h3>
                                           <ul>
                                                  <li>
                                                          <p>2014</p>
                                                          <h4>Bac S</h4>
                                                          <span>Lycée André Boulloche</span>
                                                  </li>
                                     </ul>
                                  </section>
        
                              </section>
        
                              <section id="divers" class="mainsection">
                                 <h2>Divers</h2>
           <!-- Section Langues -->
                                       <section>
                                             <h3>Langues</h3>
                                              <div class="competences">
                                                   <ul>
                                                        <li class="w100"><span>Arabe</span></li>
                                                        <li class="w80"><span>Anglais</span></li>
                                                        <li class="w60"><span>Italien</span></li>
                                               </ul>
                                          </div>
                                        </section>
        
                                      <!-- Section centres d'intérêts -->
                                  <section>
                 <h3>Centres d'intérêts</h3>
                                           <ul>
                                                  <li>Football, Basket Ball</li>
                                                  <li>Voyages</li>
                                                  <li>Musique et cinéma</li>
                                             </ul>
        
                                      </section>
        
                            </section>
                    </main>
                                   <!-- Pied de page -->
                  <footer>
                  </footer>
        
               </body>
        </html>'''
        return cv
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')


