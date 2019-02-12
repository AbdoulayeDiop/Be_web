conf = Import('../data/config.py')
chemin = conf.chemin()


def index():
    if "nom" in COOKIE:
        cv = '''<!DOCTYPE html>
        <html lang="fr">
           <head>
                        <meta charset="utf-8">
                      <title>Amine Bouamrene</title>
                       <link type="text/css" rel="stylesheet" href="''' + chemin + '''/assets/css/cv_amine.css" />

           </head>
               <body>
                        <!-- Section Identité -->
                     <header>
                                      <h1>Amine Bouamrene</h1>
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
                                                  <li>12 rue Jacqueline Auriol, Toulouse</li>
                                   <li>06 65 46 70 56</li>
                                                   <li><a href="mailto:abouamrene@gmail.com">abouamrene@gmail.com</a></li>
                                             </ul>
                                 </address>
                        </section>

                              <!-- Section Profil -->
                               <section id="profil" class="mainsection">
                                 <h2>Profil</h2>
                                       <p>Elève ingénieur à la recherche d'un stage en entreprise</p>
                           </section>

                              <!-- Section Expériences -->
                          <section id="experiences" class="mainsection" >
                                        <h2>Projets réalisés</h2>

                                      <!-- Section Expérience 1  -->
                                        <section>
                                 <div class="dates">Novembre 2017-Janvier 2018</div>
                                             <h3>Conception d'un Tétris</h3>

                                              <div class="ss-titre">ENAC <span>Toulouse</span></div>

                                              <div class="fonction">
                                                      <p>Développeur</p>
                                                  <ul>
                                                          <li>Recherche d'une fonction d'évaluation pour le jeu</li>
                                                  </ul>
                                         </div>
                                                <div class="competences">
                                                   <ul>
                                                             <li class="w100"><span>Python</li>
                                                             <li class="w80"><span>Management de projet</span></li>
                                                             <li class="w60"><span>Travail en équipe</span></li>

                                                      </ul>
                                                 </div>

                                  </section>
                                     <!-- FIN Section Expérience 1 -->

                                      <!-- Section Expérience 2 -->
                                 <section>
                                         <div class="dates">Septembre 2016-Juillet 2017</div>
                                                 <h3>Projet TIPE</h3>

                                                      <div class="ss-titre">Lycée Marcelin Berthelot<span>Saint-Maur-Des-Fossés</span></div>

                                                      <div class="fonction">
                                                          <p> Réalisation d'un colloscope </p>
                                                          <ul>
                                                                  <li>Programmation par contraintes</li>
                                                                  <li>Utilisation du solveur IBM-ILOG-CP</li>
                                                            </ul>
                                                 </div>
                                                        <div class="competences">
                               <ul>
                                                                   <li class="w100"><span>Informatique</span></li>
                                                                   <li class="w80"><span>Maths</span></li>

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
                                                           <p>2014 - 2017</p>
                                                            <h4>CPGE Scientifique MPSI/MP</h4>
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
                                                          <span>Lycée International Alexandre Dumas, Alger</span>
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
                                                        <li class="w60"><span>Espagnol</span></li>
                                               </ul>
                                          </div>
                                        </section>

                                      <!-- Section centres d'intérêts -->
                                  <section>
                 <h3>Centres d'intérêts</h3>
                                           <ul>
                                                  <li>Football, Volley-Ball</li>
                                                  <li>Voyages</li>
                                                  <li>Jeu d'échecs</li>
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


