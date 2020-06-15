import 'dart:async';
import 'dart:developer';

// import 'package:sams/models/user.dart';
import 'package:sams/models/course_info.dart';
import 'package:sams/models/user_info.dart';
import 'package:sams/services/user_token.dart';
// import 'package:sams/models/course.dart';
import 'package:sams/utils/network_util.dart';

class RestDatasource {
  static const BASE_URL = "http://192.168.43.132:8000/db_api/";
  static const LOGIN_URL = BASE_URL + "api_token_auth/";
  static const USER_DATA_URL = BASE_URL + "get_user_data/";
  static const LIST_COURSES = BASE_URL + "list_courses/";
  static const COURSE_INFO_URL = BASE_URL + "retrieve_course/";
  static const _API_KEY = "somerandomkey";

  Future<dynamic> login(String email, String password) {
    log(LOGIN_URL);
    return NetworkUtil.post(LOGIN_URL, 
    body: {
      "email": email,
      "password": password,
    }
    ).then((dynamic res) {
      log('Response From $LOGIN_URL $res');
      return res['token'];
      // UserToken.setToken(res["token"]);
    })
    .catchError((error){
      throw (error);
    })
    ;
  }

  Future<UserInfo> getUserData(){
    return NetworkUtil.get(USER_DATA_URL,
    headers: {
      "Authorization" : "Token "+UserToken.token,
    }
    ).then((response){
      return UserInfo.fromJson(response);
    }).catchError((error){
      log(error.toString());
      throw error;
    });
  }

  Future<CourseInfo> getCourseInfo(String courseCode){
    return NetworkUtil.get(COURSE_INFO_URL+courseCode,
    headers: {
      "Authorization" : "Token "+UserToken.token,
    }
    ).then((response){
      return CourseInfo.fromJson(response);
    }).catchError((error){
      log(error.toString());
      throw error;
    });
  }



}