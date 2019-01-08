<!DOCTYPE html>
<html>
<head>
	<title>Controlando leds com PHP no Raspberry</title>
</head>
<body>
<form method="GET">
	<input type="submit" name="acende" value="acende">
	<input type="submit" name="apaga" value="apaga">
</form>
</body>
</html>
<?php
if (isset($_GET['acende'])){
	shell_exec("sudo python /var/www/html/led/acende.py");
}
else {
	shell_exec("sudo python /var/www/html/led/apaga.py");
}
?>