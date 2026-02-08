<%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2025/10/22
  Time: 15:03
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
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
            height: 300px;
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

<form action="/untitled_war/add" method="post">
    <h3>添加品牌</h3>
    品牌名称：<input name="brandName"><br>
    企业名称：<input name="companyName"><br>
    排序：<input name="ordered"><br>
    描述信息：<textarea rows="5" cols="20" name="description"></textarea><br>
    状态：
    <input type="radio" name="status" value="0">禁用
    <input type="radio" name="status" value="1">启用<br>
    <input type="submit" value="提交">
</form>
</body>
</html>
