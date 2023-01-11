<script type="text/javascript">
window.onload = function () {
    var i = 5;
    var timer = setInterval(function () {
        i--;
        document.getElementById('timer').innerHTML = 'До подтверждения "Ознакомления" осталось секунд: ' + i;
        if (i == 0) {
            document.getElementById('example').style.display = 'block';
            document.getElementById('timer').style.display = 'none';
            clearInterval(timer);
        }
    }, 1000)
}
</script>