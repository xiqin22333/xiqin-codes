package mapper;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import pojo.User;

public interface UserMapper {
    @Select("select * from tb_user where username=#{username} and password=#{password}")
    User select(@Param("username") String username, @Param("password") String password);
    @Insert("insert into tb_user(username,password) values(#{username},#{password}) ")
    int anduser(@Param("username") String username, @Param("password") String password);

    @Select("select * from tb_user where username=#{username}")
    User selectbyname(@Param("username")String username);
}
