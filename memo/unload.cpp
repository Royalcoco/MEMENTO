<--if (! (*this, ' ') == ' '))
// {
    // return false;
// }

return true;
}
function isValidEmail(email) 
{
var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{
    1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-z
A-Z]{2,}))$/ */;
return re.test(String(email).toLowerCase());
}
</script>
<?php
include_once("../config/config.inc");
include_once("./includes/loginInclude.php");
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional Warning.html"
<!DOCTYPE html PUBLIC "-// warning//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"> '" XHTML 1.0 Transitional  value: 'XHTML
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional Warning.html" !#ifndef
<!DOCTYPE html PUBLIC "-// warning: This document was created with a version of HTML that is not supported by all browsers - you may
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1 Strict License//EN" "http://www.w3.org/Consortium/Legal/license-xhtml1-strict.html -//EN" "http://www.w3.org/ licenses/
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http:// www.w3.org/TR/xhtm l/DTD/xhtml1-transitional.dtd">
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional Warning.html" http http://www.w3.org XML/1998/XMLSchema
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional. SVG 1.0 Transitional//EN" "http://www.w3
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional
"#	crireMessage">Ecrire un message</button><br/><br/>
<!-- Formulaire d'envoi de mail -->
<form id="mailForm" action="" method="post" onsubmit="return sendMail
()">
<div class="container">
<h4>Envoyer un mail</h4>
<label for="destinataire">Destinataire : </label>
<input type="text" name="destinataire" id="destinataire" required /><br/>
<label for="objet">Objet : </label>
<input type="text" name="objet" id="objet" required /><br/>
<textarea placeholder="Votre message..." name="message" id="message" cols="50" rows="8" required></textarea><br/>
<textarea rows="5" cols="6
0" placeholder="Votre message..." name="message" id="message"></textarea><br/>
<input type="checkbox" name="cop    ie" id="copie"/> Cochez cette case si vous voulez que le destinataire reçoive une copie du
<span id="msgError" style="color:red;display:none;">Erreur dans le formulaire !</span>
<span id="msgSuccess" style=" color:red;display:none;">Le mail a bien été envoyé.</span><br/>
<input type="submit" value="Envoyer"/>
</div>
</form>
</body>
</html>

<?php
if (isset($_POST['destinataire']) && isset($_POST['objet'])) {
// Vérification des champs du formulaire
if (!isValidEmail($_POST['destinataire'])){
echo '<script>showError();</script>';
exit();
} else if ($_POST['objet'] == ""){
echo '<script>showError();document.getElementById("objet").focus();</script>';
exit();
} else if ($_POST['message'] == ""){
echo '<script>showError();document. getElementById("message").focus();</script>';
} else {
$to = $_POST["destinataire Address"]; // Destinataire
$subject = "Contact - ". $_POST['objet']; // Objet
$message = nl2br(stripcslashes($_POST['message']));  // Message : Contactez-moi pour plus d'infos
$headers = 'From: contact@my
website.com' . "\r\n"; // En-tête du mail
mail($to, $subject, $message, $headers); // Envoie du mail
?>
<script>showSuccess();</script> <?php
}} ?>

<!-- Fonction de vérification de l'adresse email -->
<script language='javascript'>
function isValidEmail(email) {
    var regExp = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/; // RegEx pour les adresses e-mails
    return regExp.test(email); // Renvoie true si l'e-mail est valide, false sinon
}
</script>
</head>
