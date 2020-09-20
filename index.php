<html>
<body>

<?php
 
$resultat = 0;

if(isset($_GET['request']) && !empty($_GET['request'])){
    $var1 = $_GET['request'];
    
    if((substr($var1, 0, 6) != "ADDNEW") && (substr($var1, 0, 6) != "GENLIC")) {
        $resultat = shell_exec("python3 server_sqlite.py $var1");
    }
   
    if(substr($var1, 0, 6) == "RECPAS") {
        $comp = "~";
        $i = strpos($var1, $comp);
        $to = substr($var1, 7, $i - 7);
        $lang = substr($var1, 6, 1);
        if ($lang == "0") {
            $subject = "[SET] Reset your password";
            $message = utf8_decode("Hello,
You sent a request to reset your password
Please copy the following string into SET
$resultat 

Regards

Cyberens support");
        }
        else {
            $subject = "[SET] Réinitialiser votre mot de passe";
            $message = utf8_decode("Bonjour,
Vous avez demandé à réinitialiser votre mot de passe
Veuillez copier la chaîne suivante dans SET
$resultat 

Cordialement,

Le support technique de Cyberens");
        }
        $headers = "MIME-Version: 1.0\r\n";
        $headers .= "Content-type: text/plain; charset=\"iso-8859-1\"\r\n";
        $headers .='Content-Transfer-Encoding: 8bit'."\r\n";
        $headers .= 'From: Cyberens <no-reply.set@cyberens.fr>'."\r\n";
        mail($to, $subject, $message, $headers);
    }
    else {
        echo "<pre>";
        print_r($resultat);
        echo "</pre>";
    }
    
    $mbox = imap_open ("{ssl0.ovh.net:993/imap/ssl}", "no-reply.set@cyberens.fr", "IlFaut100Rappeler") or die("Can't connect to server: " . imap_last_error());
    $headers = imap_headers ($mbox);
    if ($headers == false) {
        echo "Erreur !\n";
    } 
    else {
        while (list ($key,$val) = each ($headers)) {
            $header=imap_headerinfo($mbox, $key+1);
            $from = $header->from;
            $address = $from[0]->mailbox . "@" . $from[0]->host;
            if ((($header->Recent == 'N') || ($header->Unseen == 'U')) && ($address == 'processing@shareit.com' || $from[0]->host == 'cyberens.fr')) {
                $text = quoted_printable_decode(imap_fetchbody($mbox, $key+1, 1));
                $i = 0;
                while($i < strlen($text)) {
                    if (substr($text, $i, 18) == 'Number of licenses') {
                        $i = $i + 18;
                        while($text[$i] == ' ' || $text[$i] == '=') {
                            $i++;
                        }
                        $j = $i;
                        $numlic = '';
                        while($text[$j] != ' ' && ord($text[$j]) != 13) {
                            $numlic .= $text[$j];
                            $j++;
                        }
                    }
                    else if (substr($text, $i, 8) == 'Language') {
                        $i = $i + 8;
                        while($text[$i] == ' ' || $text[$i] == '=') {
                            $i++;
                        }
                        $j = $i;
                        $language = '';
                        while($text[$j] != ' ' && ord($text[$j]) != 13) {
                            $language .= $text[$j];
                            $j++;
                        }
                    }
                    else if (substr($text, $i, 6) == 'E-Mail') {
                        $i = $i + 6;
                        while($text[$i] == ' ' || $text[$i] == '=') {
                            $i++;
                        }
                        $j = $i;
                        $email = '';
                        while($text[$j] != ' ' && ord($text[$j]) != 13) {
                            $email .= $text[$j];
                            $j++;
                        }
                    }
                    $i++;
                }
                if ($language == 'French') {
                    if (intval($numlic) < 10) {
                        $var1="GENLIC100".$numlic.$email;
                    }
                    else if (intval($numlic) < 100) {
                        $var1="GENLIC10".$numlic.$email;
                    }
                    else {
                        $var1="GENLIC1".$numlic.$email;
                    }
                        
                }
                else {
                    if (intval($numlic) < 10) {
                        $var1="GENLIC000".$numlic.$email;
                    }
                    else if (intval($numlic) < 100) {
                        $var1="GENLIC00".$numlic.$email;
                    }
                    else {
                        $var1="GENLIC0".$numlic.$email;
                    }
                }
                $resultat = shell_exec("python3 server_sqlite.py $var1");
                $to = substr($var1, 10);
                $lang = substr($var1, 6, 1);
                if ($lang == "0") {
                    $subject = "[SET] Your licence numbers";
                    $message = utf8_decode("Hello,
Below you will find your license numbers
$resultat 

Best regards,

Cyberens support");
                }
                else {
                    $subject = "[SET] Vos numéros de licence";
                    $message = utf8_decode("Bonjour, 
Vous trouverez ci-dessous vos numéros de licence : 
$resultat 
            
Cordialement, 

Le support technique de Cyberens");
                }
                $headers = "MIME-Version: 1.0\r\n";
                $headers .= "Content-type: text/plain; charset=\"iso-8859-1\"\r\n";
                $headers .='Content-Transfer-Encoding: 8bit'."\r\n";
                $headers .= 'From: Cyberens <no-reply.set@cyberens.fr>'."\r\n";
                mail($to, $subject, $message, $headers);
            }
        }
    }
    imap_close($mbox);
    
}
else {
   echo "<pre>";
   print_r($resultat);
   echo "</pre>";
}

?>
</body>
</html>