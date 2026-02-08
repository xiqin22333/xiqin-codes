package controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import pojo.User;
import service.UserService;
import util.CheckCodeUtil;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.servlet.http.*;
import java.io.IOException;

@Controller
public class UserController {
    @Autowired
    UserService userService;

    @RequestMapping("/kkk")
    public ModelAndView handleLogin(String username, String password, String remember, HttpServletRequest req, HttpServletResponse resp)throws IOException {
        ModelAndView mav = new ModelAndView();
        if (username == null || password == null ) {
            mav.setViewName("redirect:/login.jsp");
            return mav;
        }
        User user = userService.selectall(username, password);
        if (user != null) {
            if ("1".equals(remember)){
                Cookie c_user = new Cookie("username",username);
                Cookie c_pass = new Cookie("password",password);
                c_user.setMaxAge(60*60*24*7);
                c_pass.setMaxAge(60*60*24*7);
                resp.addCookie(c_user);
                resp.addCookie(c_pass);
            }
            HttpSession session = req.getSession();
            session.setAttribute("user", user);
            mav.setViewName("redirect:/brand");
        }else  {
            mav.addObject("login_msg","用户密码错误");
            mav.setViewName("forward:/login.jsp");
        }
        return mav;
    }
    @RequestMapping("/zc")
    public String handleRegistration(String username, String password,String checkCode,HttpSession session,RedirectAttributes redirectAttributes)throws IOException {
        String checkCodeGen = (String)session.getAttribute("checkCodeGen");
        if (checkCodeGen ==null || !checkCodeGen.equalsIgnoreCase(checkCode)) {
            redirectAttributes.addFlashAttribute("register_msg","验证码错误");
            return "redirect:/register.jsp";
        }
        int result = userService.zc(username, password);
        if (result != 0) {
            redirectAttributes.addFlashAttribute("register_msg", "注册成功");
            return "redirect:/login.jsp";
        }else {
            redirectAttributes.addFlashAttribute("register_mag", "用户名已存在");
            return "redirect:/register.jsp";
        }
    }

    @RequestMapping("/checkCodeServlet")
    public void generateCheckCode(HttpServletResponse response,HttpSession session) throws IOException {
        response.setContentType("image/jpeg");

        response.setHeader("Pragma", "No-cache");
        response.setHeader("Cache-Control", "no-cache");
        response.setDateHeader("Expires", 0);

        String checkCode = CheckCodeUtil.outputVerifyImage(100,50,response.getOutputStream(),4) ;
        session.setAttribute("checkCode", checkCode);
    }

}
