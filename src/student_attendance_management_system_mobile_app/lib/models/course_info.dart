class CourseInfo {
  String _name;
  String _code;
  int _relativeAttendanceForOneLecture;
  int _relativeAttendanceForOneTutorial;
  int _relativeAttendanceForOnePractical;
  List<Instructors> _instructors;
  List<TeachingAssistants> _teachingAssistants;
  List<RegisteredStudents> _registeredStudents;
  int _acadYearStart;
  int _acadYearEnd;
  int _semester;
  int _totalLecturesHeld;
  int _totalTutorialsHeld;
  int _totalPracticalsHeld;

  CourseInfo(
      {String name,
      String code,
      int relativeAttendanceForOneLecture,
      int relativeAttendanceForOneTutorial,
      int relativeAttendanceForOnePractical,
      List<Instructors> instructors,
      List<TeachingAssistants> teachingAssistants,
      List<RegisteredStudents> registeredStudents,
      int acadYearStart,
      int acadYearEnd,
      int semester,
      int totalLecturesHeld,
      int totalTutorialsHeld,
      int totalPracticalsHeld}) {
    this._name = name;
    this._code = code;
    this._relativeAttendanceForOneLecture = relativeAttendanceForOneLecture;
    this._relativeAttendanceForOneTutorial = relativeAttendanceForOneTutorial;
    this._relativeAttendanceForOnePractical = relativeAttendanceForOnePractical;
    this._instructors = instructors;
    this._teachingAssistants = teachingAssistants;
    this._registeredStudents = registeredStudents;
    this._acadYearStart = acadYearStart;
    this._acadYearEnd = acadYearEnd;
    this._semester = semester;
    this._totalLecturesHeld = totalLecturesHeld;
    this._totalTutorialsHeld = totalTutorialsHeld;
    this._totalPracticalsHeld = totalPracticalsHeld;
  }

  String get name => _name;
  set name(String name) => _name = name;
  String get code => _code;
  set code(String code) => _code = code;
  int get relativeAttendanceForOneLecture => _relativeAttendanceForOneLecture;
  set relativeAttendanceForOneLecture(int relativeAttendanceForOneLecture) =>
      _relativeAttendanceForOneLecture = relativeAttendanceForOneLecture;
  int get relativeAttendanceForOneTutorial => _relativeAttendanceForOneTutorial;
  set relativeAttendanceForOneTutorial(int relativeAttendanceForOneTutorial) =>
      _relativeAttendanceForOneTutorial = relativeAttendanceForOneTutorial;
  int get relativeAttendanceForOnePractical =>
      _relativeAttendanceForOnePractical;
  set relativeAttendanceForOnePractical(
          int relativeAttendanceForOnePractical) =>
      _relativeAttendanceForOnePractical = relativeAttendanceForOnePractical;
  List<Instructors> get instructors => _instructors;
  set instructors(List<Instructors> instructors) => _instructors = instructors;
  List<TeachingAssistants> get teachingAssistants => _teachingAssistants;
  set teachingAssistants(List<TeachingAssistants> teachingAssistants) =>
      _teachingAssistants = teachingAssistants;
  List<RegisteredStudents> get registeredStudents => _registeredStudents;
  set registeredStudents(List<RegisteredStudents> registeredStudents) =>
      _registeredStudents = registeredStudents;
  int get acadYearStart => _acadYearStart;
  set acadYearStart(int acadYearStart) => _acadYearStart = acadYearStart;
  int get acadYearEnd => _acadYearEnd;
  set acadYearEnd(int acadYearEnd) => _acadYearEnd = acadYearEnd;
  int get semester => _semester;
  set semester(int semester) => _semester = semester;
  int get totalLecturesHeld => _totalLecturesHeld;
  set totalLecturesHeld(int totalLecturesHeld) =>
      _totalLecturesHeld = totalLecturesHeld;
  int get totalTutorialsHeld => _totalTutorialsHeld;
  set totalTutorialsHeld(int totalTutorialsHeld) =>
      _totalTutorialsHeld = totalTutorialsHeld;
  int get totalPracticalsHeld => _totalPracticalsHeld;
  set totalPracticalsHeld(int totalPracticalsHeld) =>
      _totalPracticalsHeld = totalPracticalsHeld;

  CourseInfo.fromJson(Map<String, dynamic> json) {
    _name = json['name'];
    _code = json['code'];
    _relativeAttendanceForOneLecture =
        json['relative_attendance_for_one_lecture'];
    _relativeAttendanceForOneTutorial =
        json['relative_attendance_for_one_tutorial'];
    _relativeAttendanceForOnePractical =
        json['relative_attendance_for_one_practical'];
    if (json['instructors'] != null) {
      _instructors = new List<Instructors>();
      json['instructors'].forEach((v) {
        _instructors.add(new Instructors.fromJson(v));
      });
    }
    if (json['teaching_assistants'] != null) {
      _teachingAssistants = new List<TeachingAssistants>();
      json['teaching_assistants'].forEach((v) {
        _teachingAssistants.add(new TeachingAssistants.fromJson(v));
      });
    }
    if (json['registered_students'] != null) {
      _registeredStudents = new List<RegisteredStudents>();
      json['registered_students'].forEach((v) {
        _registeredStudents.add(new RegisteredStudents.fromJson(v));
      });
    }
    _acadYearStart = json['acad_year_start'];
    _acadYearEnd = json['acad_year_end'];
    _semester = json['semester'];
    _totalLecturesHeld = json['total_lectures_held'];
    _totalTutorialsHeld = json['total_tutorials_held'];
    _totalPracticalsHeld = json['total_practicals_held'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['name'] = this._name;
    data['code'] = this._code;
    data['relative_attendance_for_one_lecture'] =
        this._relativeAttendanceForOneLecture;
    data['relative_attendance_for_one_tutorial'] =
        this._relativeAttendanceForOneTutorial;
    data['relative_attendance_for_one_practical'] =
        this._relativeAttendanceForOnePractical;
    if (this._instructors != null) {
      data['instructors'] = this._instructors.map((v) => v.toJson()).toList();
    }
    if (this._teachingAssistants != null) {
      data['teaching_assistants'] =
          this._teachingAssistants.map((v) => v.toJson()).toList();
    }
    if (this._registeredStudents != null) {
      data['registered_students'] =
          this._registeredStudents.map((v) => v.toJson()).toList();
    }
    data['acad_year_start'] = this._acadYearStart;
    data['acad_year_end'] = this._acadYearEnd;
    data['semester'] = this._semester;
    data['total_lectures_held'] = this._totalLecturesHeld;
    data['total_tutorials_held'] = this._totalTutorialsHeld;
    data['total_practicals_held'] = this._totalPracticalsHeld;
    return data;
  }
}

class Instructors {
  ClassEventCoordinator _classEventCoordinator;
  String _instructorId;

  Instructors(
      {ClassEventCoordinator classEventCoordinator, String instructorId}) {
    this._classEventCoordinator = classEventCoordinator;
    this._instructorId = instructorId;
  }

  ClassEventCoordinator get classEventCoordinator => _classEventCoordinator;
  set classEventCoordinator(ClassEventCoordinator classEventCoordinator) =>
      _classEventCoordinator = classEventCoordinator;
  String get instructorId => _instructorId;
  set instructorId(String instructorId) => _instructorId = instructorId;

  Instructors.fromJson(Map<String, dynamic> json) {
    _classEventCoordinator = json['class_event_coordinator'] != null
        ? new ClassEventCoordinator.fromJson(json['class_event_coordinator'])
        : null;
    _instructorId = json['instructor_id'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this._classEventCoordinator != null) {
      data['class_event_coordinator'] = this._classEventCoordinator.toJson();
    }
    data['instructor_id'] = this._instructorId;
    return data;
  }
}

class ClassEventCoordinator {
  User _user;

  ClassEventCoordinator({User user}) {
    this._user = user;
  }

  User get user => _user;
  set user(User user) => _user = user;

  ClassEventCoordinator.fromJson(Map<String, dynamic> json) {
    _user = json['user'] != null ? new User.fromJson(json['user']) : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this._user != null) {
      data['user'] = this._user.toJson();
    }
    return data;
  }
}

class User {
  String _firstName;
  String _lastName;
  String _email;

  User({String firstName, String lastName, String email}) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._email = email;
  }

  String get firstName => _firstName;
  set firstName(String firstName) => _firstName = firstName;
  String get lastName => _lastName;
  set lastName(String lastName) => _lastName = lastName;
  String get email => _email;
  set email(String email) => _email = email;

  User.fromJson(Map<String, dynamic> json) {
    _firstName = json['first_name'];
    _lastName = json['last_name'];
    _email = json['email'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['first_name'] = this._firstName;
    data['last_name'] = this._lastName;
    data['email'] = this._email;
    return data;
  }
}

class TeachingAssistants {
  ClassEventCoordinator _classEventCoordinator;
  String _teachingAssistantId;

  TeachingAssistants(
      {ClassEventCoordinator classEventCoordinator,
      String teachingAssistantId}) {
    this._classEventCoordinator = classEventCoordinator;
    this._teachingAssistantId = teachingAssistantId;
  }

  ClassEventCoordinator get classEventCoordinator => _classEventCoordinator;
  set classEventCoordinator(ClassEventCoordinator classEventCoordinator) =>
      _classEventCoordinator = classEventCoordinator;
  String get teachingAssistantId => _teachingAssistantId;
  set teachingAssistantId(String teachingAssistantId) =>
      _teachingAssistantId = teachingAssistantId;

  TeachingAssistants.fromJson(Map<String, dynamic> json) {
    _classEventCoordinator = json['class_event_coordinator'] != null
        ? new ClassEventCoordinator.fromJson(json['class_event_coordinator'])
        : null;
    _teachingAssistantId = json['teaching_assistant_id'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this._classEventCoordinator != null) {
      data['class_event_coordinator'] = this._classEventCoordinator.toJson();
    }
    data['teaching_assistant_id'] = this._teachingAssistantId;
    return data;
  }
}

class RegisteredStudents {
  User _user;
  String _entryNumber;

  RegisteredStudents({User user, String entryNumber}) {
    this._user = user;
    this._entryNumber = entryNumber;
  }

  User get user => _user;
  set user(User user) => _user = user;
  String get entryNumber => _entryNumber;
  set entryNumber(String entryNumber) => _entryNumber = entryNumber;

  RegisteredStudents.fromJson(Map<String, dynamic> json) {
    _user = json['user'] != null ? new User.fromJson(json['user']) : null;
    _entryNumber = json['entry_number'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this._user != null) {
      data['user'] = this._user.toJson();
    }
    data['entry_number'] = this._entryNumber;
    return data;
  }
}
