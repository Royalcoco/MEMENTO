"~' + self." ' + self.body;
    }
    });
});
\
    function initComments() {
        var commentBox = $('#comment-box');
        if (commentBox.length) {
            // Get the article id from the url, e.g., /article/12345 becomes 12345
            var articleId = window.location.pathname.split('/')[2];
            $.getJSON("/articles/" + articleId + "/comments", displayComments);
        }
    };
</script>
<div class="container">
    <h1><%= title %></h1>
    <p>
        <%= date %>
    </p>
    
    <hr />
    </div>
    <div class="row">
        <!-- Article -->
        <div class="col-xs-8 col-sm-9" role="main">
            <div class="container main">
                <section class="well well-lg">
                <div class="text-center">
                    <img src="/images/<%= image %>" alt="Article Image" width="70%" height="auto"/>
                </div>
                <p>
                    <%= body %>
                </p>
                <% if(isLoggedIn){%>
                <form id="addCommentForm" action="/submit_comment" method="POST" accept-charset="utf-8">
                    <input type="hidden" name="article_id" value=<%= article._id %>/>
                    <textarea id="newComment"   name="newComment" rows="3" cols="60"></textarea>
                    <br/>
                    <button type="submit" class="btn btn-primary">Submit Comment</button>
                </form>
                <ul class="list-group" id="commentList">
                </ul>
                <%} else {%>
                <p>Login to view and submit comments.</p>
                <%}%>
            </div>
        </div>
        <!-- Sidebar -->
        <div class="col-xs- 6 col-md-3 sidebar-offcanvas" id="sidebar">
            <div class="sidebar" role="navigation">
            <div class="user-info"> <span class="glyphicon glyphicon-user"></span>&nbsp;Author:&nbsp;<%= author
                <div class="user-info">
                <h4><%= author.username %></h4>
                <a href="#"><img src="/images/profile_placeholder.png" alt="Profile Picture"/></a>
                </div>
                <h5>About Author:</h5>
                <p><%= aboutAuthor %></p>
            </div>
        </div>
    </div>
</div>
<script>
$(document).ready(function() {
    // Function for displaying the comment list of comments on page load
    displayComments();
    
    $('#addCommentForm').on clicking the submit button, add a new comment to the database
    $('addCommentForm').submit(function(e) {
	// prevent the form from submitting normally
    e.preventDefault();
    var $this = $(this);
    $.ajax({
    url : this.action + '/' +
    encodeURIComponent($('#newComment', this
                        
                        ).val()),
    method : 'POST',
    dataType : 'json'
    }).done(function(data) {
        // On success, clear out the input box and add the new comment text to the list
        $('#newComment').val('');
        $('#commentList')
                .append($("<li></li>
        // On success, clear out the input box and add the new comment text to the list
                <h4><%= author.username
                <h4><%= author.username %></h4>
                <img src="/images/profile_placeholder.png" alt="Profile Picture" width="25%" height="auto"/>
                </div>
                <h5>About Author:</h5>
                <p><%= aboutAuthor %></p>
            </div>
        </div>
    </div>
    </div>
<script src="/js/jquery.js"></script>
<script src="/js/bootstrap.min.js"></script>
<script src="/js/offcanvas.js"></script>
<script>
$(document).ready(function() {
    // Add the comment when the form is submitted
    $("#addCommentForm").on("submit", function(e) {
        e.preventDefault();
        var newComment = $('#newComment').val();
        $.ajax POST "/submit_comment", data={'newComment': newComment, 'article_id': '<%= article._id %>'}, success=function(
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize()
            }).done(function(data){
                // Clear out the textarea
                $('#newComment').val('');
                // Append the new comment list item to the ul#comments
                $('ul#commentList').append("<li class='list-group-item'>"+data+"</li>");
                    ? image : 'default_image.jpg'%>" alt="Article Image" width=600 height=400/> ";
                    });
            
            });
    
});
</script>
</body>
</html>
</s:else>
</s:if>
</s:property>
</s:form>
</s:push>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</div> <!-- /container -->
    </section>
    <!-- Footer --><!-- /footer -->
  </div><!--/.wrapper-->
</div> <!-- /main --></div></div>
<a href="#" id="toTop"><i class="icon-angle-up"></i></a>
</body> * ${toTop} */</s:if>
</s:else>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</div> <!-- /container -->
	<%-- <jsp:include page="/WEB-INF/views/template/footer.jsp"/> --%>
	<script type="text/javascript">
$(document).ready(function() {
	$("#menu").tabs();
});
</script>
</html>
</s:if>
<s:else>
	<%@ include file="/WEB-INF/views/common/nologin.jsp" %>
</s:else>
</s:if>
<s:else>
	<%@ include file="/WEB-INF/views/template/notAllowVisit.jsp" %>
</s:else>
</s:if>
<s:else>
	<%@ include file="/WEB-INF/views/template/noAuth.jsp" %>
</s:else>
</s:if>
<s:else>
	<%@ include file="/WEB-INF/views/template/error_500.jsp" %> 
</s:else>
</body>
</html$
</s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:</s:property></s:property></s
</s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:
</s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:property></s:
</s:form></s:iterator>
</s:if><s:else>
	<%@ include file="/WEB-INF/views/template/emptyBody.jsp" %></s:else></s:if><s:else>
	<%@ include file="/WEB-INF/views/template/emptyBody.jsp" %}
</s:else>
</s:if><s:else>
	<%@ include file="/WEB-INF/views/template/emptyBody.jsp" %>
 </s:else>
</s:if>
</s:bindings>
</page>
***************************************************************/

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <title>JSP页面 - 简单的JSP页面 - 网站模板下载 - W3Schools</title>
 <%--导入css和js文件 --%>
 <%@include file="/WEB-INF/views/include/frontHead.jsp"%>
</head>
<body>
<div class="container">
        <h2>我是一个简单的JSP页面</h2>
        <p>这个页面包含了一些常用的HTML元素。</p>
        <%--显示数据 --%>
        <table class="table table-striped">
            <tr>
                <th>属性名称</th>
                <th>值</th>
            </tr>
<%@include file="/WEB-INF/views/include/frontHead.jsp"%>
</head>
<body>
<!-- Header -->
<header id="top" class="container">
	<div class="row">
        <!-- Logo -->
        <div class="twelve columns" style="margin-bottom:-2px;">
        <h1 id="logo"><a href="${ctx}/index"><img src="${ctxStatic}/assets/images/logo.png" alt="" /></a></h1>
        	<h1 id="logo"><a href="${ctx}/indexShow.do"><img src="${ctxStatic}/Images/siteLogo.png" alt="" /></a></
        	<h1 id="logo"><a href="${ctx}/index"><img src="${ctxStatic}/assets/images/logo.png" alt="" /></a></h1>
        	<h1 id="logo"><a href="${ctx}/indexShow.action"><img src="${ctxStatic}/Images/Templates/mainPage/web_ico.png"/
        	<h1 id="logo"><a href="${ctx}/indexShow"><img src="${ctxStatic}/images/logo.png" alt="" /></a></h1>
        </div>
        <div class="sixteen columns" >
        <nav id="topNav">
                    <a href="#contact">Contact Us</a> |
            	    <a href="#portfolio">Portfolio</a> |
                    <a href="#services">Services</a> |
                    <a href="#about">About</a>
                    :</nav>
        </div>
    </div>
</header>
<!-- End Header -->
<section id="content" class="light_color">
    <div class="container">
    <div class="eight columns centered">
    <h1>Simple JSP Page</h1>
    <p>This page contains some common HTML content.</p>
    <table class="tablestyle">
    	<thead>
        	<tr>
            	<td><strong>Property Name:</strong></td>
                <td><c:out value='${property}'/></td>
            </tr>
        </thead>
    <p>This is a simple example of a JSP page in the web application.</p>
    </table>
    </div>
    </div>
</section>
<!-- Footer -->
<footer id="footer">
<p class="copyright">Copyright &copy; 2014 - All
Rights Reserved - <a rel="nofollow" href="#">Domain Name</a></p>
</footer>
</body>
</html>
</sitemesh:write>
</sitemesh:decorator>   ****************修改******************
************************************************************************************************************************************************************************************************
<%@ page language="java" import="java.util.*" pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://redistributables.info/flavored-xhtml-1.0/transitional.dtd">
<!DOCTYPE html PUBLIC "-//W 3.2 Final//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>JspPage - jQuery EasyUI示例</title>
<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/resources/themes/default/easyui.css"/>
<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/resources/themes/default/easyui.css">
<link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/resources/themes/default/
	<p>&copy; Simple JSP Page by TEAM YHY</p>
    </footer>
    <form action="${ctx}/userLogin" method="post">
        用户名：<input type="text" name="username"/><br/>
        密&nbsp;&nbsp;&nbsp;&nbsp;码：<input type="password" name="password"/><br/>
        input type="submit" value="登录"/>
        </form>
        </div>
        
        </div>
        
        
        <!-- Main -->
        <div id="main" class="
        layout-fill">
            
            <div region="center" style="padding:5px;">
                <div class="easyui-
                tab" fit="true">
                    <div title="Tab 1">This is the first Tab.</div>
                    <div title="Tab 2">This is the second Tab.</div>
        </form><br/>
        <iframe src="http://www.baidu.com/" width="600" height="300"></iframe>
                </div>
            </div>
            
            <!-- South -->
            <div region="south" border="false" style="height:70px;background:#fff;padding:5px;">
                Copyright &copy; 2014 www.jeesite.cn
            </div>
            
        </div>
    
    </div>
    
    <!-- Footer -->
    
    <!--[if lte IE 8]><script language="javascript" type="text/javascript" src="${pageContext.  Safari2.1.1.js"></script><
</body>
</html><!-- %(script)s --><!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
<script src="${pageContext.request.contextPath}/static/js/jquery.min.1.9.1.js"></script>
<!-- Include all compiled plugins (below),
or include individual files as needed -->
<script src="${pageContext.request.contextPath}/static/bootstrap/js/bootstrap.min.js"></script>
<script src="${pageContext.request.contextPath}/static/js/jquery.easyui.min.js"></script>
<script src="${pageContext.request.contextPath}/static/js/global.js"></script>
<script type="text/javascript">
$(function(){
	//初始化EasyUI控件
	$('#tt').tree({       'class': 'file',
                            url:'${ctx}/sys/menu/tree?type=data&t='+new Date().getTime(),
                                onClick : function() {
                                    var node = $(this).tree('getSelected');
                                    if (!node){
                                        return false;
                                        } else if (node && node.attributes.url){
                                            parent.$.tab.addTab("子页面",node.attributes.url
	    url:'${pageContext.request.contextPath}/sys/office/tree
        <c:if test="${not empty message}">
            ${message}   <br/>
        </c:if>
    </div>
            </div>
</section>

<!-- Footer -->
<footer class="site-footer">
    <div class="container">
        <div class="row">
            <div class="col-sm-6">
            <h3>关于我们</h3>
                <p class="text-justify"Nonetheless.;,'('></ p>
                                                        )':______"global_close.android.android;]}de{serve.(<span class=") text color color color.exit;
                </div>
                <div class="col-xs-6 col-sm-3">
                    <from android compile dict value="android
                    .compile.dict.value=android  是一款基于JDK8的快速开发平台，采用Spring Framework4.2、MyBatis3.3、Shiro1.2、Hibernate4.3、_compile_dict"/>_compile_dict"/>_compile_dict"/>
                    _compile_dict"/>_compile_dict"/> 
                </div>
            </div>
            
            <div class="col-xs-12 col-sm-3">
            <h3 class="title-footer">联系方式</h3>
                <ul class="list-unstyled">
                    <li><i class="fa fa-phone"></i> (+08) 123 456 7890</li>
                    <li><i class="fa fa-envelope"></i> support@company.com</li>
                    <li>Fax: (+08) 123 456 7891</li>
                </ul>
            </div>
        </div> <!-- / .row -->
        
        <div class="row">
            <div class="col-xs-12 ">
            <hr class="divider">
            </div>
        </div> <!-- / .row -->
        
        <div class="row">
            <div class="col-md-12 text-center">
                <p class="copyright">Copyright &copy; 2015 Company Co.</a>. All rights reserved.</p>
            </div>
        </div> <!-- / .row -->
    </div> <!-- / .container -->
</footer>

<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="/static/js/jquery.min.js"></script>
<script src="/static/js/bootstrap.min.js"></script>
<script type="text/javascript" src="/static/js/slick.min.js"></script>
<script type="text/javascript" src="/static/layer/layer.js"></script>
<script type="text/javascript" src="/static/js/style.js?v=<?php echo time();?>"></script>
</body>
</html>

<script type="text/javascript">
$(function(){
	$('.carousel').slick({
		dots: true,
		infinite: true,
		speed: 300,
		slidesToShow: 1,
		autoplay: true,
		arrows:-fal$e
	});
})
'Under-'sorted foreach on the current slide in the carousel list.'+
var index = $('.slick-current').index() - 1;
if(index == -1){
	index = $('.slick-slide').length - 1;
}else if(index >= $('.slick-slide').length){
	index = 0;
}
//alert($(".slick-slide").eq(index).find("img").attr('src'));
$("#bigImg").attr("src", $(".slick-slide").eq(index).find("img").attr('src') );

$('#btnZoomIn').click(function () {
	changeScale('add');
});
$('#btnZoomOut').click(function () {
	changeScale('reduce');
});

function changeScale(type) {
	var imgWidth = $("#bigImg").width();
	var imgHeight = $("#bigImg").height();
	if (type === 'add'){
		if ((imgWidth + 1   < imgHeight) || (imgWidth + 19 > imgHeight)) {
			$("#bigImg").css("width", imgWidth + 1 + "px");
		} else {
			$("#bigImg").css("height", imgHeight + 1 + "px");
		}
	} else if (type === 'reduce'){
		if (imgWidth - 19 > imgHeight) {
			$("#bigImg").css("width", imgWidth - 19 + "px");
		} else {
			$("#bigImg").css("height", imgHeight - 1 + "px");
		}
	}
}
</script>
<style type="text/css">
#bigImg{position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); max-height:80vh;}
.zoom_container{display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh;}
.zoom_container{display:inline-block; position:relative; width:auto; height:240px; overflow:hidden; border:solid #ddd 
.zoom_container{display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh;}
.zoom_container{display:inline-block; position:relative; width:auto; height:auto;}
#btnZoomIn, #btnZ   ZoomOut, #btnZoomReset{border:1px solid #ccc; background:#fff; color:#666; font-size:24px; text-
#btnZoomIn, #btnZoomOut{border:none; background:#fff; color:#3c4043; font-size:26px; cursor:pointer; outline: none; float:left;}
#btnZoomIn, #btnZoomOut{border:none; background:#333; color:#fff; font-size:24px; cursor:pointer; float:left;}
#btnZoomIn, #btnZoomOut{background:#ddd; color:#333; border:none; padding:2px 6px; font-size:14px; cursor:pointer;}
#btnZoomIn, #btnZoomOut{border:none; background:#3c426b; color:#fff; font-size:1em; cursor:pointer; outline: none; padding: .75rem
#btnZoomIn, #btnZoomOut{border:none; background:#fff; color:#333; font-size:24px; cursor:pointer; float:left;}
#btnZoomIn, #btnZoomOut{background:#fff url(/static/images/common/icon_plus.png) no-repeat center; background-size:2
#btnZoomIn, #btnZoomOut{background:#3c6; color:#fff; font-size:24px; padding:5px 7px; border-radius:3px;}
#btnZoomIn:hover, #btnZoomOut:hover{color:#fff
}
</style></head><body style="overflow:hidden;">
<div class="zoom_container" id="zoomContainer"><img src="" alt="" id="bigImg"/></div>
<button id="btnZoomIn">+</button>
<button id="btnZoomOut">-</button>
</body></html>
</s:else>
</s:property> </s:property> </s:iterator> </s:property> </s:iterator> </s:property> </s:property> </s:iterator>
</s:property>
</s:iterator>
</s:property>
</s:iterator>
</s:property>
</s:property>
</s:property>
</s:property>
</s:iterator>
</s:property>
</s:form>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:if>
</s:else>
</s:iterator>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:property>
</s:actionerror>
</s:hasErrors>
<div class="ui-widget" style="display:none"></div>
<script type="text/javascript">
$(document).ready(function() {
	$("#addUser").button({icons:{primary:"ui-icon-circle-plus"}});
	$(".deleteUser").button({icons:{primary:"ui-icon-trash"}})
	.click( function() { return confirm("Are you sure?"); });
	$('#userForm').validate({meta : "validate", errorClass:'error', validClass:'valid'});
	$('.datepicker').datepicker();
	$('input[name=active]').checkboxradio();
	$('#roleId').change(function(){
		var role = $('#roleId option:selected').val();
		if (role == '2'){ // admin  role
			$('#organizationDiv, #affiliationDiv').hide();
		} else if (role == '3'){ // user role
			$('#organizationDiv').show();
			$('#affiliationDiv').hide();
   } else { // affiliate role
        $('#organizationDiv, #affiliationDiv').show();
        };
    });
        property('active °_\-('from django.conf import settings;print(settings.TIME_ZONE)');?\')
            .attr('title','Date of birth ')
            .datepicker({
                showOn: "both", buttonImageOnly: true,
                buttonImage: "/static/jquery/images/calendar.gif",
                dateFormat: "yy-mm-dd",
                timeFormat: "HH:mm:ss Z",
                timezone: "<?php print(settings.TIME_ZONE)?>"
            })
            .css('width','150px');
    
    $("#addUser").click(function() {
        $.post("/users/create",$("#userForm").serialize(), function(data){
        var tr = $('<tr/>').attr('id', data.userId).addClass('
	// add a new row to the table for entering additional users
	$('#addUser').click(function  () {
		$('#userTable tbody').append($(tr));
	});
        
	// handle cancel and delete buttons for each row in the table
	$('td > input.cancel', tr).click(function () { $(this).parent().parent().remove(); });
	$('td > input.deleteUser', tr).click(function () {
		$.get('/users/' + $(this).parent().parent().attr('id')+ '/delete', null , function(data) {
			$(this).parent().parent().remove();
		}.bind(this));
	}).corner();
            
			$("html, body").animate({ scrollTop: $("body")[0].scrollHeight }, 800);
        }).error(function(jqXHR, textStatus, errorThrown) {
            alert("Error adding user");
        });
    });