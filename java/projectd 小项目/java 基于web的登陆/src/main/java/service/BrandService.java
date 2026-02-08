package service;

import mapper.BrandMapper;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import pojo.Brand;
import util.mybatisUtil;

import java.beans.Transient;
import java.io.IOException;
import java.util.List;
@Service
public class BrandService {
    @Autowired
    BrandMapper brandMapper;
    public List<Brand> slectebrands() throws IOException {
        List<Brand> brands= brandMapper.selectall();
        return brands;
    }
@Transactional
public int add(String brandName,String companyName,int ordered,String description,int status) throws IOException {
    int i= brandMapper.addbrand(brandName,companyName,ordered,description,status);
    return i;
}
@Transactional
public int delete(int id) throws IOException {
    int i= brandMapper.delete(id);
    return i;
}
 public Brand sbid(int id) throws IOException {
     Brand brand= brandMapper.selectbrandbyid(id);
     System.out.println(brand);
     return brand;
 }
 @Transactional
 public int updete(String brandName,String companyName,int ordered,String description,int status,int id) throws IOException {
     int i= brandMapper.updatebrand(brandName,companyName,ordered,description,status,id);
     System.out.println(i);
     return i;
 }
}
