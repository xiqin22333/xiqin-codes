package mapper;

import org.apache.ibatis.annotations.*;
import pojo.Brand;

import java.util.List;

public interface BrandMapper {
    //查询
    @Select("select * from tb_brand")
    @ResultMap("selectb")
    List<Brand> selectall();
    //增加
    @Insert("insert into tb_brand(brand_name,company_name,ordered,description,status) values(#{brandname},#{compnyname},#{order},#{dc},#{status})")
    int addbrand(@Param("brandname") String brandname,
                 @Param("compnyname")String compnyname,
                 @Param("order")int order,
                 @Param("dc")String dc,
                 @Param("status")int status);
    //修改
    @Update("update tb_brand set brand_name=#{bm},company_name=#{cm},ordered=#{od},description=#{dp},status=#{st} where id=#{id}")
    int updatebrand(@Param("bm") String bm,
                    @Param("cm")String cm,
                    @Param("od")int od,
                    @Param("dp")String dp,
                    @Param("st")int st,
                    @Param("id")int id);
    //根据id查询
    @Select("select * from tb_brand where id=#{id}")
    @ResultMap("selectb")
    Brand selectbrandbyid(@Param("id") int id);

    //根据id删除
    @Delete("delete from tb_brand where id=#{id}")
    int delete(@Param("id")int id);
}
