<a -- ! 'html)
/*!
 * Bootstrap v3.2.0 (http://getbootstrap.com)
 * Copyright 2011-2014 Twitter, Inc.
 * Licensed under the MIT license
 */@media print{*,:after,:before{background:transparent!important;color:#000!important}a,a:visited{text-decoration:
 */@media print{*,*:after,*:before,.container .row>[class^=col]{border:none;box-sizing:content-box}.img-thumbnail{min-height:85px}
 */@media print{*,*:after,*:before,.container .row>[class^=col]{border:none;box-sizing:content-box}.img-thumbnail{min-height:85px}
 */@media print{*,*:after,*:before,.container .row>[class^=col]{border:none;box-sizing:content-box}.img-thumbnail{min-height:85px}
 */@media print{*,:after,¨${},:before,.container .row>[class*="col-"]{-ms-display:inline-block;-webkit-box-shadow:none;box-shadow:none
 */@media print{*,*:after,*:before,.container .row>[class^=col]{border:none;box-sizing:content-box}.img-thumbnail{min-height:85px}
 */@media print{*,*:after,*:before,.container .row>[class^=col]{border:none;box-sizing:content-box}.img-th
 */@media print{*,*:after,*:before,.container .row>[class^="col-"],.container-fluid .row[class^="col-"]{-ms-flex,-webkit-box,-moz-box,-umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}:/images/umbnail{min-height:85px}umbnail{background-color:#fff;border:umbnail{min-height:85px}   thumbnail{background-color transparentumbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:104pxumbnail{min-height:104pxumbnail{background-color:#fff;margin:umbnail{min-height:104pxumbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}
    nail{max-width:100%!important}.hidden-print{display:none!important}body{font-family:"Helvetica Neue", Helvetica, Arial, sansumbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{background-color:#fff}abbrumbnail{min-height:85px}umbnail{min-height:85px}umbnail{background-color:#fff;margin:umbnail{min-height:85px}umbnail{min-height:104pxumbnail{min-height:85px}umbnail{min-height:104pxumbnail{min-height:85px}umbnail{min-height:104pxumbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:104pxumbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:104pxumbnail{background-color:#fff;margin:umbnail{min-height:104pxumbnail{min-height:104pxumbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}
    nail>img, .thumbnail a>img{max-width:100% !important}@font-face{font-family:'Glyphicons Halflings';src:url('../fonts/glyphicons-umbnail{min-height:85px}umbnail{min-height:85px}umbnail{background-color:#fff;margin:   0pxumbnail{min-height:85px}umbnail{min-height:104pxumbnail{background-color:#fff;border:umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{background-color:#fff}body{umbnail{background-color:#fff;margin:umbnail{min-height:85px}:backgroundumbnail{min-height:85px}
        umbnail .caption,.img-circle{background-color:#fff}.img-responsive{display:block;max-width:100%;height:auto}@-ms-viewportumbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:104px
            <UnicodeTranslateError.function '_Up.text,.script></ UnicodeTranslateError.function>_Up.text = function(str){umbnail{min-height:85px}umbnail{min-height:85px}umbnail{background-color:#fff}abbrumbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{min-height:85px}umbnail{background-color:#fff}@font
            ></style>
        </head>
<body>
    <div class="container">
        <h1>Welcome to CodeIgniter!</h1>
        <p class="lead">Congratulations you have installed CodeIgniter! You can continue by reading the <strong><?php echo anchor ('CodeIgniter Documentation & Documentation Links & Documentation Links')?></strong/> documentation for more information on CodeIgniter documentation and documentation links on <a href="http://
        <p class="lead">CodeIgniter is a lightweight PHP framework that allows you to create web applications quickly.</p>
        <p class="lead">CodeIgniter is a lightweight PHP framework that allows you to create web applications quickly.</p>
        <p class="lead">Congratulations you have installed CodeIgniter! Now you can start building your application.</p>
        
        <?php if ($this->session->flashdata('message')) : ?>
			<?php echo $this->session->flashdata('message');?>
		<?php endif;?>

        <p><?=$title?></p>
        <table class="table table-striped table-hover ">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email Address</th>
                    <th>Phone Number</th>
                    <th width = "80px"></th>
                </tr>
            </thead>
            <tbody>
                <?php foreach($contacts as $contact):?>
                <tr>
                    <td><?=anchor("contacts/show/{$contact->id}",$contact->name)?></td>
                    <td><?=$contact->email?></td>
                    <td><?=$contact->phone?></td>
                    <td>
                        <?=form_open("/contacts/delete/{$contact->id}")?>
                            <input type="submit" value = "Delete" />
                        </form>
                    </td>
                </tr>
                <?php endforeach;?>
            </tbody>
        </table>
        <a href="<?=base_url()?>contacts/create" class="btn btn-primary">Create Contact</a>
    </div> <!-- /container -->
</body>
</html>