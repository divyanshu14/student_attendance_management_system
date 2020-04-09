import 'dart:async';
import 'dart:developer';

import 'package:sams/utils/network_util.dart';
import 'package:sams/models/user.dart';

class RestDatasource {
  NetworkUtil _netUtil = new NetworkUtil();
  static final BASE_URL = "http://192.168.43.132:8000/api/v1/db/";
  static final LOGIN_URL = BASE_URL + "login/";
  static final _API_KEY = "somerandomkey";

  Future<User> login(String username, String password) {
    return _netUtil.post(LOGIN_URL, 
    
    body: {
      "token": _API_KEY,
      "username": username,
      "password": password
    }
    ).then((dynamic res) {
      log(res.toString());
      if(res["token"]==null) {
        log('token not received');
        throw  Exception (res["non_field_errors"]);
      }	
      User user_data= new User.map({
      "username": username,
      "password": password}
      );
      log(user_data.username);
      return user_data;
    })
    .catchError((error){
      throw new Exception(error);
    })
    ;
  }
}