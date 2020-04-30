
// import 'package:sams/models/student.dart';

// import 'instructor.dart';

class Course{
  String name;
  String code;

  Course({this.name, this.code});

  Course.fromJson(Map<String, dynamic> json) {
    name = json['name'];
    code = json['code'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['name'] = this.name;
    data['code'] = this.code;
    return data;
  }
}