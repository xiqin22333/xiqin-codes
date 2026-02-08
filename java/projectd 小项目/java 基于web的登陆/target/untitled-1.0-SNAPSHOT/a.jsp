<%@ page import="pojo.Brand" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.ArrayList" %><%--
  Created by IntelliJ IDEA.
  User: Administrator
  Date: 2025/10/17
  Time: 11:07
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Title</title>
    <style>
        body{
            background-image: url("imgs/1.jfif");
            background-repeat: no-repeat;
            background-size: 100% 100%;
            background-attachment: fixed;
        }
        table{
            position: fixed;
            left: 200px;
        }
        table td{
            height: 70px;
        }
        table tr:nth-child(odd){
            background-color:beige;
            opacity: 0.5;
        }
        table tr:nth-child(even){
            background-color:honeydew;
            opacity: 0.5;
        }
        th{
            background-color: #FFFFFF;
        }
        .c{
            display: block;
            float: left;
            width: 50px;
            height: 25px;
            background-color:#6bf3ff;
            margin-left: 20px;
            border: 2px solid #6bf3ff;
            border-radius: 10px;
            text-decoration: none;
            color: #aaaaaa;

        }
        .d{
            display: block;
            float: left;
            width: 50px;
            height: 25px;
            background-color:#ffd51b;
            margin-left: 20px;
            border: 2px solid #ffd51b;
            border-radius: 10px;
            text-decoration: none;
            color: #aaaaaa;

        }
        .a,.b{
            width: 150px;
        }
        h1{
            position: relative;
            top: 20px;
            left: 850px;
        }
        .f{
            position: relative;
            top: 87px;
            left:200px;
        }
    </style>
</head>
<body>
<input class="f" type="button" value="新增" id="add"><br>
<h1>${user.username},欢迎您</h1>
<hr>
<table  width="800">
    <tr class="e">
        <th>序号</th>
        <th>品牌名称</th>
        <th>企业名称</th>
        <th>排序</th>
        <th>品牌介绍</th>
        <th>状态</th>
        <th class="b">操作</th>
    </tr>

    <c:forEach items="${brands}" var="brand" varStatus="status">
        <tr align="center">
            <td>${status.count}</td>
            <td>${brand.brandName}</td>
            <td>${brand.companyName}</td>
            <td>${brand.ordered}</td>
            <td>${brand.description}</td>
            <c:if test="${brand.status==1}">
                <td>启用</td>
            </c:if>
            <c:if test="${brand.status==0}">
                <td> 禁用</td>
            </c:if>
            <td class="a">
                <a href="/untitled_war/byid?id=${brand.id}" class="c">修改</a>
                <a href="/untitled_war/delete?id=${brand.id}" class="d">删除</a>
            </td>
        </tr>
    </c:forEach>


</table>
<script>
    document.getElementById("add").onclick = function (){
        location.href = "/untitled_war/addBrand.jsp";
    }
</script>
</body>
</html>
