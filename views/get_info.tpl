<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>qr-code</title>

    <script src="bower_components/jquery/dist/jquery.js"></script>
    <script src="bower_components/bootstrap/dist/js/bootstrap.js"></script>
    <script src="bower_components/js/responsive.js"></script>

    <link href="bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" media="screen">
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
