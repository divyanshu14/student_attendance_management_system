
class UserInfo {
  User user;
  // List<Null> userPermissions;
  // List<String> rolePermissions;
  List<Course> instructorForCourses;
  List<Course> teachingAssistantForCourses;
  List<Course> studentForCourses;


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
      teachingAssistantForCourses = new List<Course>();
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
class User {
  String _firstName;
  String _lastName;
  String _email;
  Student _student;
  Classeventcoordinator _classeventcoordinator;

  User(
      {String firstName,
      String lastName,
      String email,
      Student student,
      Classeventcoordinator classeventcoordinator}) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._email = email;
    this._student = student;
    this._classeventcoordinator = classeventcoordinator;
  }

  String get firstName => _firstName;
  set firstName(String firstName) => _firstName = firstName;
  String get lastName => _lastName;
  set lastName(String lastName) => _lastName = lastName;
  String get email => _email;
  set email(String email) => _email = email;
  Student get student => _student;
  set student(Student student) => _student = student;
  Classeventcoordinator get classeventcoordinator => _classeventcoordinator;
  set classeventcoordinator(Classeventcoordinator classeventcoordinator) =>
      _classeventcoordinator = classeventcoordinator;

  User.fromJson(Map<String, dynamic> json) {
    _firstName = json['first_name'];
    _lastName = json['last_name'];
    _email = json['email'];
    _student =
        json['student'] != null ? new Student.fromJson(json['student']) : null;
    _classeventcoordinator = json['classeventcoordinator'] != null
        ? new Classeventcoordinator.fromJson(json['classeventcoordinator'])
        : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['first_name'] = this._firstName;
    data['last_name'] = this._lastName;
    data['email'] = this._email;
    if (this._student != null) {
      data['student'] = this._student.toJson();
    }
    if (this._classeventcoordinator != null) {
      data['classeventcoordinator'] = this._classeventcoordinator.toJson();
    }
    return data;
  }
}

class Student {
  String _entryNumber;

  Student({String entryNumber}) {
    this._entryNumber = entryNumber;
  }

  String get entryNumber => _entryNumber;
  set entryNumber(String entryNumber) => _entryNumber = entryNumber;

  Student.fromJson(Map<String, dynamic> json) {
    _entryNumber = json['entry_number'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['entry_number'] = this._entryNumber;
    return data;
  }
}

class Classeventcoordinator {
  Teachingassistant _teachingassistant;

  Classeventcoordinator({Teachingassistant teachingassistant}) {
    this._teachingassistant = teachingassistant;
  }

  Teachingassistant get teachingassistant => _teachingassistant;
  set teachingassistant(Teachingassistant teachingassistant) =>
      _teachingassistant = teachingassistant;

  Classeventcoordinator.fromJson(Map<String, dynamic> json) {
    _teachingassistant = json['teachingassistant'] != null
        ? new Teachingassistant.fromJson(json['teachingassistant'])
        : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this._teachingassistant != null) {
      data['teachingassistant'] = this._teachingassistant.toJson();
    }
    return data;
  }
}

class Teachingassistant {
  String _teachingAssistantId;

  Teachingassistant({String teachingAssistantId}) {
    this._teachingAssistantId = teachingAssistantId;
  }

  String get teachingAssistantId => _teachingAssistantId;
  set teachingAssistantId(String teachingAssistantId) =>
      _teachingAssistantId = teachingAssistantId;

  Teachingassistant.fromJson(Map<String, dynamic> json) {
    _teachingAssistantId = json['teaching_assistant_id'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['teaching_assistant_id'] = this._teachingAssistantId;
    return data;
  }
}

class Course {
  String _name;
  String _code;

  Course({String name, String code}) {
    this._name = name;
    this._code = code;
  }

  String get name => _name;
  String get code => _code;

  Course.fromJson(Map<String, dynamic> json) {
    _name = json['name'];
    _code = json['code'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['name'] = this._name;
    data['code'] = this._code;
    return data;
  }
}
