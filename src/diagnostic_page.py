# -*- coding: utf-8 -*-
"""Self-contained Greek Burnout Diagnostic (vanilla JS port of diagnostic.jsx)."""

TITLE = "Burnout Diagnostic — δωρεάν τεστ αυτοαξιολόγησης"
DESC = ("Δωρεάν εργαλείο αυτοαξιολόγησης (~8′): δες αν αυτό που περνάς μοιάζει με burnout, "
        "σε ποιο επίπεδο και πού να εστιάσεις. Ενδεικτικό, όχι κλινική διάγνωση.")

DIAG_STYLE = """
<style>
#diag-app .eyebrow{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#666;line-height:1.7}
#diag-app .dh1{font-size:32px;font-weight:400;line-height:1.35;margin-bottom:1.5rem}
#diag-app .dp{margin-bottom:1.4rem;line-height:1.75;font-size:18px}
#diag-app .note{font-size:14px;color:#777;line-height:1.7}
#diag-app .dcard{border:1px solid rgba(40,39,38,.15);padding:1rem;border-radius:8px}
#diag-app .opt{width:100%;text-align:left;border:1px solid rgba(40,39,38,.15);padding:1rem;border-radius:8px;background:transparent;color:#282726;font-family:inherit;font-size:16px;line-height:1.7;cursor:pointer;margin-bottom:.75rem;transition:border-color .12s,background .12s}
#diag-app .opt:hover{border-color:rgba(26,127,55,.6);background:rgba(26,127,55,.04)}
#diag-app .opt.sel{border:1px solid #1a7f37;background:#1a7f37;color:#fff}
#diag-app .qh{font-size:20px;line-height:1.85;margin-bottom:1.8rem;font-weight:400}
#diag-app .pline{height:1px;background:rgba(40,39,38,.12);margin-top:.8rem}
#diag-app .pfill{height:1px;background:#1a7f37;transition:width .2s ease}
#diag-app .nav{display:flex;justify-content:space-between;gap:1rem;margin-top:2rem}
#diag-app input[type=email]{width:100%;border:1px solid rgba(40,39,38,.2);padding:1rem;border-radius:8px;background:transparent;color:#282726;font-family:inherit;font-size:15px;outline:none}
#diag-app .drow{border:1px solid rgba(40,39,38,.15);padding:1rem;border-radius:8px;margin-bottom:.75rem}
#diag-app .grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:2rem 0}
@media(max-width:860px){#diag-app .dh1{font-size:24px}#diag-app .grid3{grid-template-columns:1fr}}
</style>
"""


def render(head, sidebar, footer, mobile_nav, JS, rel):
    d = 1
    slug = "burnout-diagnostic"
    ft = footer(d)
    inner = (head(TITLE, DESC, slug, d, "img/og/burnout-diagnostic.png", bc="Burnout Diagnostic")
             + '<div id="root">'
             + sidebar(slug, d)
             + '<div id="main-scroll"><main class="wrap">'
             + DIAG_STYLE
             + '<div id="diag-app"></div>'
             + '</main></div></div>'
             + mobile_nav(slug, d)
             + JS
             + DIAG_JS.replace("__FOOTER__", ft.replace("\\", "\\\\").replace("`", "\\`").replace("</", "<\\/"))
             + "\n</body>\n</html>\n")
    return inner


DIAG_JS = r"""
<script>
(function(){
  var BOOK = { mail: "mailto:aggelos.mouzakitis@gmail.com?subject=Burnout%20Diagnostic" };
  var SHEET_URL = "https://script.google.com/macros/s/AKfycby-gv3oCFT2q5KXvVnqRzS4PAzcMjPB8Gls5qodZJ3v4_9HKGqJHMdBCw7YYbEzIE2d/exec";
  var FOOTER = `__FOOTER__`;

  var SECTIONS = [
    {id:'self-worth', title:'Αυτοεκτίμηση μέσω επιτευγμάτων', key:'self_worth', q:[
      'Μια κακή περίοδος στη δουλειά μπορεί να επηρεάσει σημαντικά την αυτοπεποίθησή μου.',
      'Όταν δεν τα πάω καλά επαγγελματικά, τείνω να γίνομαι πιο σκληρός/ή με τον εαυτό μου.',
      'Είναι πιο εύκολο να νιώθω καλά με τον εαυτό μου όταν πάνε καλά τα επαγγελματικά.']},
    {id:'shame-guilt-pressure', title:'Ντροπή, ενοχή και πίεση', key:'shame_guilt_pressure', q:[
      'Δυσκολεύομαι να χαλαρώσω όσο υπάρχει ακόμα δουλειά να γίνει.',
      'Μπορεί να κάτσω να ξεκουραστώ και να νιώθω ότι θα έπρεπε να είμαι παραγωγικός/ή.',
      'Τείνω να εστιάζω σε αυτό που ακόμα λείπει.']},
    {id:'comparison', title:'Σύγκριση και αίσθημα ανεπάρκειας', key:'comparison', q:[
      'Το να βλέπω άλλους να τα πάνε καλά με κάνει να ανησυχώ για την απόδοσή μου.',
      'Όταν κάποιος κοντινός μου προχωράει γρήγορα, σκέφτομαι πού υστερώ.',
      'Μπορεί να έχω αντικειμενικά καλά αποτελέσματα και να νιώθω πίσω από τους στόχους μου.']},
    {id:'vulnerability', title:'Φόβος ευαλωτότητας', key:'vulnerability', q:[
      'Νιώθω άβολα με την ιδέα να με δουν αδύναμο/η άνθρωποι κοντινοί μου.',
      'Αν δυσκολεύομαι, το ένστικτό μου είναι συνήθως να το κρατήσω για μένα.',
      'Προτιμώ να αντιμετωπίσω κάτι μόνος/η παρά να με δουν αβέβαιο/η ή «ακατάστατο/η».']},
    {id:'grind', title:'Υπερηφάνεια στην αντοχή και την πίεση', key:'grind', q:[
      'Είμαι συνηθισμένος/η να κουβαλάω πολλά χωρίς να παραπονιέμαι.',
      'Ένα κομμάτι μου υπερηφανεύεται για το πόση πίεση αντέχω.',
      'Το να επιβραδύνω μπορεί να μου φαίνεται άβολο, ακόμα κι όταν το χρειάζομαι.']},
    {id:'identity', title:'Ταυτότητα και εικόνα', key:'identity', q:[
      'Οι άνθρωποι με ξέρουν ως κάποιον/α που βγάζει τα πράγματα πέρα.',
      'Το να είμαι ικανός/ή είναι μεγάλο κομμάτι του πώς βλέπω τον εαυτό μου.',
      'Το να απογοητεύω κόσμο με χτυπάει δυνατά, ειδικά όταν περιμένουν πολλά.',
      'Μου λένε συχνά ότι είμαι πολύ σκληρός/ή με τον εαυτό μου ή ότι πιέζομαι υπερβολικά.']},
    {id:'relationships', title:'Διαπροσωπικές σχέσεις', key:'relationships', q:[
      'Όταν η δουλειά είναι βαριά, έχω λιγότερη υπομονή με ανθρώπους που δεν το καταλαβαίνουν.',
      'Όταν είμαι στρεσαρισμένος/η, γίνομαι πιο δύσκολος/η στη συναναστροφή.',
      'Υπάρχουν φορές που νιώθω τόσο φορτωμένος/η που δεν είμαι πραγματικά παρών/παρούσα με τους άλλους.',
      'Η σχέση με τον/τη σύντροφό μου έχει επηρεαστεί από το πώς κουβαλάω το άγχος.',
      'Υπάρχουν φορές που νιώθω απόμακρος/η από τον/τη σύντροφό μου, ή εκείνος/η νιώθει αστήρικτος/η.']},
    {id:'drive-meaning', title:'Απώλεια κινήτρου και νοήματος', key:'drive_meaning', q:[
      'Έχω αρχίσει να νιώθω δυσαρέσκεια για κομμάτια της δουλειάς που κάποτε με γέμιζαν.',
      'Μου λείπουν οι εποχές που η δουλειά ήταν πιο εύκολο να με ευχαριστεί.']},
    {id:'numbness', title:'Συναισθηματικό μούδιασμα και αποστασιοποίηση', key:'numbness', q:[
      'Μπορώ να περάσω μια ολόκληρη μέρα και να νιώθω συναισθηματικά «επίπεδος/η».',
      'Πράγματα που κάποτε με ενδιέφεραν δεν με αγγίζουν το ίδιο πια.',
      'Μπορώ να είμαι παραγωγικός/ή και να νιώθω αποσυνδεδεμένος/η από αυτό που κάνω.',
      'Συχνά νιώθω λιγότερο ο εαυτός μου και περισσότερο ότι απλώς «λειτουργώ».',
      'Υπάρχουν στιγμές που αναρωτιέμαι για ποιο πράγμα γίνεται όλη αυτή η προσπάθεια.']},
    {id:'cynicism', title:'Κυνισμός και αποπροσωποποίηση', key:'cynicism', q:[
      'Έχω γίνει πιο κυνικός/ή για τη δουλειά απ’ ό,τι παλιά.',
      'Κάποια κομμάτια της δουλειάς μοιάζουν πια μηχανικά, ακόμα κι όταν τα κάνω καλά.',
      'Υπάρχουν στιγμές που νιώθω πιο αποστασιοποιημένος/η παρά μέσα στο παιχνίδι.']},
    {id:'nervous-system', title:'Υπερφόρτωση νευρικού συστήματος', key:'nervous_system', q:[
      'Μπορεί να είμαι κουρασμένος/η και να μην μπορώ να «κατέβω» πραγματικά.',
      'Ο ύπνος δεν με αφήνει πάντα να νιώσω σωστά ξεκούραστος/η.',
      'Το άγχος έχει αρχίσει να εμφανίζεται σωματικά — πονοκέφαλοι, μυϊκή ένταση, στομάχι, ναυτία ή παρόμοια.',
      'Το σώμα μου μένει σε ένταση ακόμα κι όταν δεν δουλεύω ενεργά.']},
    {id:'tech-activation', title:'Διαρκής ενεργοποίηση (tech)', key:'tech_activation', q:[
      'Ακόμα κι όταν είμαι εκτός, ένα κομμάτι μου νιώθει «σε ετοιμότητα».',
      'Τσεκάρω πράγματα της δουλειάς σε στιγμές που θα έπρεπε να είναι προσωπικές.',
      'Μου είναι δύσκολο να νιώσω πλήρως εκτός υπηρεσίας.',
      'Το μυαλό μου μένει συνδεδεμένο με τη δουλειά περισσότερο απ’ ό,τι θα ήθελα.',
      'Νιώθω πίεση να απαντήσω γρήγορα, ακόμα κι όταν δεν χρειάζεται.',
      'Καταφεύγω συχνά σε AI, self-help περιεχόμενο ή παρόμοια, αλλά σπάνια οδηγεί σε πραγματική αλλαγή.',
      'Καταναλώνω συμβουλές για burnout/άγχος/απόδοση, αλλά μένω κολλημένος/η στα ίδια μοτίβα.']}
  ];

  var FLAT=[]; SECTIONS.forEach(function(s){s.q.forEach(function(t,i){FLAT.push({key:s.id+'-'+i,sec:s.title,text:t});});});
  var SCALE=[{v:1,l:'Διαφωνώ απόλυτα'},{v:2,l:'Διαφωνώ'},{v:3,l:'Ούτε συμφωνώ ούτε διαφωνώ'},{v:4,l:'Συμφωνώ'},{v:5,l:'Συμφωνώ απόλυτα'},{v:'na',l:'Δ/Α'}];

  function avg(a){if(!a.length)return null;return a.reduce(function(x,y){return x+y;},0)/a.length;}
  function fmt(s){return s===null?'N/A':s.toFixed(2);}
  function grade(s){if(s===null)return 'Ανεπαρκή δεδομένα';if(s<=2.25)return 'Επίπεδο 1 — Σταθερά, αλλά υπό πίεση';if(s<=2.9)return 'Επίπεδο 2 — Αποδίδετε με κόστος';if(s<=3.5)return 'Επίπεδο 3 — Υψηλή λειτουργικότητα, εσωτερική εξάντληση';return 'Επίπεδο 4 — Κατάρρευση της πληρότητας';}
  function desc(s){if(s===null)return 'Δεν υπάρχουν ακόμα αρκετά δεδομένα.';if(s<=2.25)return 'Λειτουργείτε ακόμα καλά, αλλά κάποια σημεία αρχίζουν να δείχνουν καταπόνηση. Δεν μιλάμε για διαχείριση κρίσης — μιλάμε για πρόληψη, επίγνωση και μικρές προσαρμογές πριν το κόστος μεγαλώσει.';if(s<=2.9)return 'Εξακολουθείτε να αποδίδετε, αλλά η επιτυχία αρχίζει να σας κοστίζει περισσότερα απ’ όσα σας δίνει. Ίσως παρατηρείτε συναισθηματική κόπωση, πιο αργή ανάκαμψη, ευερεθιστότητα, λιγότερη πληρότητα, ή μεγαλύτερη εξάρτηση από τα επιτεύγματα για να νιώσετε καλά.';if(s<=3.5)return 'Απέξω μπορεί να δείχνετε ακόμα ικανός/ή, αλλά εσωτερικά το σύστημά σας είναι υπό σημαντική πίεση. Εδώ η συναισθηματική επιπεδότητα, η αποφυγή, η ένταση στις σχέσεις και η υπερφόρτωση του νευρικού συστήματος γίνονται πιο δύσκολο να αγνοηθούν.';return 'Σε αυτό το στάδιο, το ζήτημα δεν είναι πια μόνο το άγχος. Ο τρόπος που λειτουργείτε μπορεί να έχει αποσυνδεθεί από την ευεξία, τις αξίες, το σώμα, τις σχέσεις και την αίσθηση εαυτού. Ο στόχος δεν είναι απλώς περισσότερη ξεκούραση — είναι να ξαναχτίσετε τη σχέση σας με τη φιλοδοξία και την επιτυχία.';}
  function nextStep(s){if(s===null)return '';if(s<=2.25)return 'Η χρήσιμη κίνηση εδώ είναι η πρόληψη: εντοπίστε ποιες περιοχές αρχίζουν να αντλούν ενέργεια και προσαρμόστε πριν ανέβει το κόστος.';if(s<=2.9)return 'Εδώ οι μικρές δομικές και εσωτερικές αλλαγές αποδίδουν περισσότερο — πριν το «αποδίδω με κόστος» σκληρύνει σε κάτι βαρύτερο.';if(s<=3.5)return 'Σε αυτό το επίπεδο, η διαχείριση συμπτωμάτων συνήθως δεν αρκεί. Η δουλειά είναι να δούμε τι τροφοδοτεί το φορτίο από κάτω — ταυτότητα, πίεση, ανάκαμψη — όχι απλώς να ξεκουραστείτε πιο πολύ.';return 'Δεν είναι θέμα θέλησης και η ξεκούραση από μόνη της δεν το λύνει. Η δουλειά είναι να ξαναχτίσετε τη σχέση σας με τη φιλοδοξία και την επιτυχία, ώστε να σταματήσει να σας κοστίζει τόσο.';}
  function secLabel(s){if(s===null)return 'Ανεπαρκή δεδομένα';if(s<=2.5)return 'Χαμηλό';if(s<=3.2)return 'Αυξημένο';return 'Υψηλό';}
  function levelVis(s){if(s===null)return{c:'#bbb',p:0};var p=Math.max(0,Math.min(100,((s-1)/4)*100));if(s<=2.5)return{c:'#1a7f37',p:p};if(s<=3.2)return{c:'#d9a200',p:p};return{c:'#c0392b',p:p};}

  var DIMS=[
    {id:'aw',title:'Επιτεύγματα & αυτοεκτίμηση',ids:['self-worth','comparison'],
      lo:'Η αξία σας δεν φαίνεται να κρέμεται από το τελευταίο αποτέλεσμα. Είναι μια σταθερή βάση που λίγοι high performers έχουν.',
      me:'Η αίσθηση αξίας σας στηρίζεται στα επιτεύγματα περισσότερο απ’ όσο θα θέλατε. Οι καλές περίοδοι σας ανεβάζουν, οι κακές κόβουν βαθύτερα απ’ όσο δικαιολογούν τα γεγονότα.',
      hi:'Αυτή τη στιγμή η αξία σας είναι στενά δεμένη με την απόδοση. Οι νίκες καθησυχάζουν στιγμιαία, οι αποτυχίες πονάνε προσωπικά, και ο πήχης ανεβαίνει διαρκώς. Αυτή είναι η μηχανή κάτω από πολλά υπόλοιπα.'},
    {id:'pr',title:'Πίεση & εσωτερική απαίτηση',ids:['shame-guilt-pressure','grind'],
      lo:'Μπορείτε να χαλαρώσετε χωρίς να κυβερνά η ενοχή. Η πίεση που κουβαλάτε δείχνει κυρίως εξωτερική, όχι αυτοπαραγόμενη.',
      me:'Αρκετή από την πίεσή σας είναι αυτοεπιβαλλόμενη. Η ξεκούραση έρχεται με «φόρο», και το «αρκετά» ανεβαίνει διαρκώς.',
      hi:'Το μεγαλύτερο μέρος της πίεσης έρχεται από μέσα. Το να επιβραδύνετε μοιάζει επικίνδυνο αντί για αναζωογονητικό, και η απαίτηση σπάνια υποχωρεί.'},
    {id:'iv',title:'Ταυτότητα & ευαλωτότητα',ids:['identity','vulnerability'],
      lo:'Μπορεί να σας δουν αβέβαιο/η ή να δυσκολεύεστε χωρίς να απειλείται το ποιος είστε. Αυτή η ευελιξία είναι προστατευτική.',
      me:'Το να είστε ο/η ικανός/ή και συγκροτημένος/η μετράει αρκετά ώστε να δείξετε καταπόνηση να μοιάζει ρίσκο. Μάλλον κουβαλάτε περισσότερα μόνοι σας απ’ όσο χρειάζεται.',
      hi:'Η ταυτότητά σας είναι έντονα επενδυμένη στο να είστε ικανός/ή και δύσκολο να απογοητεύσετε. Η ευαλωτότητα μοιάζει επικίνδυνη, οπότε η καταπόνηση μένει κρυμμένη — κι αυτό ακριβώς τη συντηρεί.'},
    {id:'em',title:'Συναισθηματική διαθεσιμότητα & σχέσεις',ids:['relationships'],
      lo:'Η πίεση της δουλειάς δεν φαίνεται να «στάζει» στο πόσο παρών/παρούσα είστε με τους κοντινούς σας.',
      me:'Μέρος του φορτίου περνάει στις σχέσεις σας — λιγότερη υπομονή, λιγότερη παρουσία, πιο κοντό «φυτίλι» απ’ όσο θα θέλατε.',
      hi:'Ο τρόπος λειτουργίας σας κοστίζει εκτός δουλειάς. Οι πιο κοντινοί σας μάλλον παίρνουν την εξαντλημένη εκδοχή, και αυτό το κενό τείνει να μεγαλώνει.'},
    {id:'mf',title:'Νόημα & πληρότητα',ids:['drive-meaning','numbness','cynicism'],
      lo:'Η δουλειά σάς δίνει ακόμα κάτι πίσω. Δεν λειτουργείτε απλώς με φόρα — υπάρχει πραγματική εμπλοκή.',
      me:'Η ανταμοιβή αραιώνει. Αποδίδετε ακόμα, αλλά περισσότερο μοιάζει με κίνηση παρά με νόημα, και η ικανοποίηση δεν «κάθεται» όπως πριν.',
      hi:'Αυτό μετράει περισσότερο για την πληρότητα. Η επιτυχία δεν σας ανταμείβει συναισθηματικά τώρα — επιπεδότητα, αποστασιοποίηση και «για ποιο πράγμα γίνονται όλα;» εμφανίζονται κάτω από την απόδοση.'},
    {id:'ns',title:'Φορτίο νευρικού συστήματος',ids:['nervous-system'],
      lo:'Το σώμα σας φαίνεται να ανακάμπτει αρκετά καλά. Το σύστημα δεν είναι κολλημένο σε διαρκή ενεργοποίηση.',
      me:'Το σώμα σας κρατάει ένα μέρος — ένταση, ανομοιόμορφος ύπνος, ένα «βουητό» που δεν σβήνει τελείως. Η ανάκαμψη δεν προλαβαίνει.',
      hi:'Το νευρικό σας σύστημα είναι υπό πραγματικό φορτίο. Κουρασμένος/η αλλά «σε ένταση», κακή ανάκαμψη, σωματικά συμπτώματα — το σώμα σηματοδοτεί αυτό που το μυαλό παρακάμπτει. Σπάνια λύνεται μόνο με θέληση.'},
    {id:'ta',title:'Διαρκής ενεργοποίηση (tech)',ids:['tech-activation'],
      lo:'Μπορείτε να είστε πραγματικά εκτός υπηρεσίας. Η δουλειά δεν κρατά μια μόνιμη διεργασία ανοιχτή στο μυαλό σας.',
      me:'Σπάνια είστε εντελώς εκτός. Ένα κομμάτι σας μένει «σε ετοιμότητα», τσεκάρει, μισο-συνδεδεμένο — κι αυτό μπλοκάρει σιωπηλά την πραγματική ανάκαμψη.',
      hi:'Είστε σχεδόν πάντα ενεργοποιημένος/η. Το να «κλείσετε διακόπτη» μοιάζει άπιαστο, και αυτή η διαρκής κατάσταση «on» είναι από τα δυσκολότερα μοτίβα να διακοπούν χωρίς σχέδιο.'}
  ];
  function pick(dm,s){if(s===null)return dm.me;if(s<=2.5)return dm.lo;if(s<=3.2)return dm.me;return dm.hi;}

  var state={screen:'intro',answers:{},idx:0,email:'',results:null};
  var root=document.getElementById('diag-app');
  function esc(x){return x;}
  function scoreSections(){return SECTIONS.map(function(sec){var keys=sec.q.map(function(_,i){return sec.id+'-'+i;});var nums=keys.map(function(k){return state.answers[k];}).filter(function(v){return typeof v==='number';});var ans=keys.filter(function(k){return state.answers[k]!==undefined;}).length;var th=Math.ceil(keys.length*0.7);var sc=ans>=th?avg(nums):null;return{id:sec.id,title:sec.title,key:sec.key,score:sc,label:secLabel(sc)};});}
  function scoreDims(){return DIMS.map(function(dm){var keys=[];dm.ids.forEach(function(sid){var sec=SECTIONS.filter(function(s){return s.id===sid;})[0];if(sec)sec.q.forEach(function(_,i){keys.push(sid+'-'+i);});});var nums=keys.map(function(k){return state.answers[k];}).filter(function(v){return typeof v==='number';});var ans=keys.filter(function(k){return state.answers[k]!==undefined;}).length;var th=Math.ceil(keys.length*0.7);var sc=ans>=th?avg(nums):null;return{title:dm.title,score:sc,label:secLabel(sc),interp:pick(dm,sc)};});}
  function overall(){var nums=Object.keys(state.answers).map(function(k){return state.answers[k];}).filter(function(v){return typeof v==='number';});return avg(nums);}
  function calc(){var ov=overall();var dims=scoreDims();var sorted=dims.slice().sort(function(a,b){var av=typeof a.score==='number'?a.score:-1;var bv=typeof b.score==='number'?b.score:-1;return bv-av;});var top=null;dims.forEach(function(d){if(typeof d.score==='number'&&(!top||d.score>top.score))top=d;});return{overall:ov,grade:grade(ov),desc:desc(ov),next:nextStep(ov),dims:sorted,top:top,sections:scoreSections()};}
  function postSheet(cal){try{var body={email:state.email.trim(),overall_score:fmt(cal.overall),overall_grade:cal.grade,page_url:location.href};cal.sections.forEach(function(s){body[s.key]=fmt(s.score);});fetch(SHEET_URL,{method:'POST',mode:'no-cors',body:JSON.stringify(body)}).catch(function(){});}catch(e){}}

  function render(){
    var totalQ=FLAT.length;
    var answered=Object.keys(state.answers).filter(function(k){return state.answers[k]!==undefined;}).length;
    var progress=Math.round(answered/totalQ*100);
    var h='';
    if(state.screen==='intro'){
      h+='<h1 class="dh1">Burnout Diagnostic</h1>';
      h+='<p class="dp">Σκοπός αυτού του τεστ δεν είναι να σας διαγνώσει ή να σας βάλει ταμπέλα.</p>';
      h+='<p class="dp">Το χρησιμοποιώ για να πάρω μια πρώτη εικόνα του πώς λειτουργεί σήμερα η σχέση σας με τη δουλειά, την πίεση, την ευθύνη, τις αποφάσεις, τη σύγκρουση, τη φιλοδοξία, την ανάκαμψη και τους ανθρώπους γύρω σας.</p>';
      h+='<p class="dp">Περίπου 8 λεπτά. Στο τέλος παίρνετε το μοτίβο λειτουργίας σας, ένα επίπεδο και μια ανάλυση — δείτε το περισσότερο ως αφορμή για συζήτηση.</p>';
      h+='<div class="grid3">';
      [['Διάρκεια','45 ερωτήσεις'],['Μορφή','κλίμακα 1–5 + Δ/Α'],['Αποτέλεσμα','Επίπεδο + ανάλυση']].forEach(function(x){h+='<div class="dcard"><div style="font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#6e6e6e;margin-bottom:.5rem">'+x[0]+'</div><div>'+x[1]+'</div></div>';});
      h+='</div>';
      h+='<p class="note">Το τεστ είναι ενδεικτικό, όχι κλινική διάγνωση.</p>';
      h+='<div style="margin-top:2rem"><button class="cta-btn" id="d-start">Ξεκινήστε</button></div>';
      h+=FOOTER;
    } else if(state.screen==='question'){
      var q=FLAT[state.idx];var cur=state.answers[q.key];
      h+='<div style="margin-bottom:2rem"><div style="display:flex;justify-content:space-between;gap:1rem;margin-bottom:.8rem"><p class="eyebrow">Ερώτηση '+(state.idx+1)+' από '+totalQ+'</p><p class="eyebrow">'+progress+'% ολοκληρώθηκε</p></div><div class="pline"><div class="pfill" style="width:'+progress+'%"></div></div></div>';
      h+='<h2 class="qh">'+q.text+'</h2>';
      SCALE.forEach(function(o){h+='<button class="opt'+(cur===o.v?' sel':'')+'" data-v="'+o.v+'">'+o.l+'</button>';});
      h+='<div class="nav"><button class="cta-ghost" id="d-back" '+(state.idx===0?'disabled style="opacity:.4"':'')+'>Πίσω</button>';
      h+='<button class="cta-btn" id="d-next" '+(cur===undefined?'disabled style="opacity:.4"':'')+'>'+(state.idx===totalQ-1?'Συνέχεια':'Επόμενη')+'</button></div>';
    } else if(state.screen==='gate'){
      h+='<p class="eyebrow">Ένα τελευταίο βήμα (προαιρετικό)</p>';
      h+='<h1 class="dh1">Το email σας (αν θέλετε να λάβετε το αποτέλεσμα).</h1>';
      h+='<p class="dp">Μπορείτε να δείτε το αποτέλεσμά σας αμέσως, με ή χωρίς email.</p>';
      h+='<label style="display:block;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#6e6e6e;margin-bottom:.6rem">Email (προαιρετικό)</label>';
      h+='<input type="email" id="d-email" placeholder="you@example.com" value="'+state.email.replace(/"/g,'&quot;')+'">';
      h+='<div class="nav"><button class="cta-ghost" id="d-back2">Πίσω</button><button class="cta-btn" id="d-show">Δείτε το αποτέλεσμα</button></div>';
    } else if(state.screen==='results'&&state.results){
      var r=state.results;
      h+='<p class="eyebrow">Το αποτέλεσμά σας</p>';
      h+='<h1 class="dh1" style="margin-bottom:.5rem">'+r.grade+'</h1>';
      h+='<p class="dp">Σκορ: <span style="color:#1a7f37">'+fmt(r.overall)+'</span> / 5.00</p>';
      if(r.top)h+='<p class="dp">Η περιοχή με το μεγαλύτερο φορτίο τώρα είναι <span style="border-bottom:1px solid rgba(40,39,38,.3)">'+r.top.title+'</span>.</p>';
      h+='<p class="dp">'+r.desc+'</p>';
      if(r.next)h+='<div style="border-left:2px solid #1a7f37;padding:2px 0 2px 14px;margin:1.6rem 0"><p class="eyebrow" style="margin-bottom:.5rem">Τι να το κάνετε</p><p class="dp" style="margin-bottom:0">'+r.next+'</p></div>';
      h+='<p class="note">Το τεστ είναι ενδεικτικό, όχι κλινική διάγνωση.</p>';
      h+='<div style="margin-top:2rem"><p class="eyebrow" style="margin-bottom:1rem">Το μοτίβο λειτουργίας σας <span style="color:#bbb">· μεγαλύτερο φορτίο πρώτα</span></p>';
      r.dims.forEach(function(d){var v=levelVis(d.score);h+='<div class="drow"><div style="display:flex;justify-content:space-between;gap:1rem"><div>'+d.title+'</div><div style="text-align:right;flex-shrink:0"><div style="color:'+v.c+'">'+d.label+'</div><div style="font-size:13px;color:#6e6e6e">'+fmt(d.score)+' / 5.00</div></div></div><div style="height:3px;background:rgba(40,39,38,.08);border-radius:2px;margin:.6rem 0"><div style="height:3px;width:'+v.p+'%;background:'+v.c+';border-radius:2px"></div></div><div style="font-size:13px;color:#777;line-height:1.65">'+d.interp+'</div></div>';});
      h+='</div>';
      h+='<div style="border:1px solid rgba(26,127,55,0.3);background:rgba(26,127,55,0.04);padding:1.4rem;margin-top:2.5rem"><p class="eyebrow" style="margin-bottom:.6rem">Πού πάει από εδώ</p><p class="dp" style="margin-bottom:1.2rem">Ένα τεστ δείχνει το μοτίβο. Η αλλαγή του είναι η πραγματική δουλειά. Αν κάτι από αυτά σας άγγιξε, το επόμενο βήμα είναι μια απλή επικοινωνία — να δούμε πού βρίσκεστε και αν έχει νόημα να δουλέψουμε μαζί.</p><a class="cta-btn" href="'+BOOK.mail+'">Επικοινωνία</a></div>';
      h+='<div style="display:flex;gap:1rem;margin-top:2rem;flex-wrap:wrap"><button class="cta-ghost" id="d-retake">Επανάληψη</button><button class="cta-ghost" id="d-print">Εκτύπωση</button></div>';
      h+=FOOTER;
    }
    root.innerHTML=h;
    bind();
  }
  function bind(){
    var s=document.getElementById('d-start');if(s)s.onclick=function(){state.screen='question';state.idx=0;render();window.scrollTo(0,0);};
    document.querySelectorAll('#diag-app .opt').forEach(function(b){b.onclick=function(){var v=b.getAttribute('data-v');state.answers[FLAT[state.idx].key]=(v==='na'?'na':parseInt(v,10));render();};});
    var bk=document.getElementById('d-back');if(bk)bk.onclick=function(){if(state.idx>0){state.idx--;render();window.scrollTo(0,0);}};
    var nx=document.getElementById('d-next');if(nx)nx.onclick=function(){if(state.idx<FLAT.length-1){state.idx++;render();window.scrollTo(0,0);}else{state.screen='gate';render();window.scrollTo(0,0);}};
    var b2=document.getElementById('d-back2');if(b2)b2.onclick=function(){state.screen='question';render();window.scrollTo(0,0);};
    var em=document.getElementById('d-email');if(em)em.oninput=function(){state.email=em.value;};
    var sh=document.getElementById('d-show');if(sh)sh.onclick=function(){state.results=calc();if(state.email.trim())postSheet(state.results);state.screen='results';render();window.scrollTo(0,0);};
    var rt=document.getElementById('d-retake');if(rt)rt.onclick=function(){state={screen:'intro',answers:{},idx:0,email:'',results:null};render();window.scrollTo(0,0);};
    var pr=document.getElementById('d-print');if(pr)pr.onclick=function(){window.print();};
  }
  render();
})();
</script>
"""
