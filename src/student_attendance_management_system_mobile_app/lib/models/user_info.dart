import 'package:sams/models/course.dart';
import 'package:sams/models/user.dart';

class UserInfo {
  User user;
  // List<Null> userPermissions;
  // List<String> rolePermissions;
  List<Course> instructorForCourses;
  List<Course> teachingAssistantForCourses;
  List<Course> studentForCourses;


  UserInfo(
      {this.user,
      // this.userPermissions,
      // this.rolePermissions,
      this.instructorForCourses,
      this.teachingAssistantForCourses});

  UserInfo.fromJson(Map<String, dynamic> json) {
    user = json['user'] != null ? new User.fromJson(json['user']) : null;
    // if (json['user_permissions'] != null) {
    //   userPermissions = new List<Null>();
    //   json['user_permissions'].forEach((v) {
    //     userPermissions.add(new Permissions.fromJson(v));
    //   });
    // }
    // rolePermissions = json['role_permissions'].cast<String>();
    if (json['instructor_for_courses'] != null) {
      instructorForCourses = new List<Course>();
      json['instructor_for_courses'].forEach((v) {
        instructorForCourses.add(new Course.fromJson(v));
      });
    }
    if (json['teaching_assistant_for_courses'] != null) {
      teachingAssistantForCourses = new List<Null>();
      json['teaching_assistant_for_courses'].forEach((v) {
        teachingAssistantForCourses.add(new Course.fromJson(v));
      });
    }
    if (json['student_for_courses'] != null) {
      studentForCourses = new List<Course>();
      json['student_for_courses'].forEach((v) {
        studentForCourses.add(new Course.fromJson(v));
      });
    }
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.user != null) {
      data['user'] = this.user.toJson();
    }
    // if (this.userPermissions != null) {
    //   data['user_permissions'] =
    //       this.userPermissions.map((v) => v.toJson()).toList();
    // }
    // data['role_permissions'] = this.rolePermissions;
    if (this.instructorForCourses != null) {
      data['instructor_for_courses'] =
          this.instructorForCourses.map((v) => v.toJson()).toList();
    }
    if (this.teachingAssistantForCourses != null) {
      data['teaching_assistant_for_courses'] =
          this.teachingAssistantForCourses.map((v) => v.toJson()).toList();
    }
    if (this.studentForCourses != null) {
      data['student_for_courses'] =
          this.studentForCourses.map((v) => v.toJson()).toList();
    }
    return data;
  }
}
