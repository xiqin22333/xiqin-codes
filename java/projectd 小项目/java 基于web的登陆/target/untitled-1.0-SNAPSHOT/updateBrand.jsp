<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2025/10/22
  Time: 15:03
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Title</title>
    <style>
        body{
            background-image: url("imgs/2.jfif");
            background-repeat: no-repeat;
            background-size: 100% 100%;
            background-attachment: fixed;
        }
        form{
            background-color:white;
            opacity: 0.5;
            width: 300px;
            height: 350px;
            text-align: center;
            position: relative;
            left: 400px;
            top: 100px;
            border-radius: 20px;
            box-shadow: 5px 5px 5px gainsboro;
        }
    </style>
</head>
<body>

<form action="/untitled_war/update" method="post">
    <h3>修改品牌</h3>
    <input name="id" type="hidden" value="${brand.id}"><br>
    品牌名称：<input name="brandName" value="${brand.brandName}"><br>
    企业名称：<input name="companyName" value="${brand.companyName}"><br>
    排序：<input name="ordered" value="${brand.ordered}"><br>
    描述信息：<textarea rows="5" cols="20" name="description" >${brand.description}</textarea>
    <br>
    状态：
    <c:if test="${brand.status == 0}">
        <input type="radio" name="status" value="0" checked>禁用
        <input type="radio" name="status" value="1">启用<br>
    </c:if>
    <c:if test="${brand.status == 1}">
        <input type="radio" name="status" value="0" >禁用
        <input type="radio" name="status" value="1" checked>启用<br>
    </c:if>
    <br>
    <input type="submit" value="提交">
</form>
</body>
</html>