package service;

import mapper.UserMapper;
import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import pojo.User;
import util.mybatisUtil;

import java.io.IOException;
@Service
public class UserService {
    @Autowired
    UserMapper userMapper;

    public User selectall(String username, String password) throws IOException {
        User user = userMapper.select(username, password);
        return user;
    }

    @Transactional
    public int zc(String username, String password) throws IOException {
        User user = userMapper.selectbyname(username);
        int i = 0;
        if (user == null) {
            i = userMapper.anduser(username, password);
            //提交事务
        }
        return i;
    }
}