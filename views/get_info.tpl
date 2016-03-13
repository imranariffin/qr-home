<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>qr-code</title>

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
    
    <script src="bower_components/js/responsive.js"></script>

    <!-- <link href="bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" media="screen"> -->
    <link href="static/css/main.css" rel="stylesheet" media="screen">

</head>
<body>

    <div class="container">
        <div class="header">
            <ul class="nav nav-pills pull-right">
                <li class="active"><a ng-href="#">Home</a></li>
            </ul>
            <h3 class="text-muted">qr-code</h3>
        </div>

        <div class="jumbotron">
            <h1>QR-HOME</h1>    
            <h3>Fill in the information and help your elderly stay safe!</h3>
            <p class="lead">
        <br>
        <div class="panel panel-default">
          <div class="panel-heading">Name</div>
          <div class="panel-body">
            {{name}}
          </div>
        </div>

        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">Emergency Contact</h3>
          </div>
          <div class="panel-body">
            {{contact}}
          </div>
        </div>
        <br>
        <img id="showqr" src="/static/img/imranyooo.jpg" style="display:none">
            </p>
            <p><a href="/goto-make-qr" class="btn btn-lg btn-success" ng-href="#"><span class="glyphicon glyphicon-ok"></span>Make QR</a></p>
        </div>        
    </div>
</body>
</html>
