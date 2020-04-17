class UserInfo {

  static String _username;
  static String _firstName;
  static String _lastName;
  static bool _adminPermissions;
  static bool _isStudent;
  static bool _isTeacher;
  static bool _isTA;

  UserInfo.map(dynamic obj) {
    _username = obj["username"];
    _firstName = obj["first_name"];
    _lastName = obj["last_name"];
    _adminPermissions = obj["admin_permissions"];
    _isStudent = obj["is_student"];
    _isTeacher = obj["is_teacher"];
    _isTA = obj["is_ta"];
  } 

  String get username => _username;
  String get firstName => _firstName;
  String get lastName => _lastName;
  bool get adminPermissions => _adminPermissions;
  bool get isTA => _isTA;
  bool get isTeacher => _isTeacher;
  bool get isStudent => _isStudent;
 
//TODO: implment to map function


}