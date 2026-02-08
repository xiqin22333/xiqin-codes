package controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import pojo.Brand;
import service.BrandService;

import java.io.IOException;
import java.util.List;

@Controller
public class BrandController {
    @Autowired
    BrandService brandService;

    @RequestMapping("/add")
    public String addBrand(String brandName,String companyName,int ordered,String description,int status)throws IOException,IOException {
        brandService.add(brandName,companyName,ordered,description,status);
        return "redirect:/brand";
    }

    @RequestMapping("/brand")
    public String getBrands(Model model)throws IOException{
        List<Brand> brands = brandService.slectebrands();
        model.addAttribute("brands",brands);
        return "/a.jsp";
    }

    @RequestMapping("/delete")
    public String deleteBrand(int id)throws IOException{
        brandService.delete(id);
        return "redirect:/brand";
    }

    @RequestMapping("/update")
    public String updateBrand(String brandName,String companyName,int ordered,String description,int status,int id)throws IOException{
        brandService.updete(brandName,companyName,ordered,description,status, id);
        return "redirect:/brand";
    }

    @RequestMapping("/byid")
    public ModelAndView getBrandById(int id)throws IOException{
        Brand brand = brandService.sbid(id);
        ModelAndView mav = new ModelAndView();
        mav.addObject("brand",brand);
        mav.setViewName("forward:/updateBrand.jsp");
        return mav;
    }
}
