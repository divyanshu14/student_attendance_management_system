
class ClasseventCoordinator {
  Instructor instructor;
  TeachingAssistant teachingassistant;

  ClasseventCoordinator({this.instructor, this.teachingassistant});

  ClasseventCoordinator.fromJson(Map<String, dynamic> json) {
    instructor = json['instructor'] != null
        ? new Instructor.fromJson(json['instructor'])
        : null;
    teachingassistant = json['teachingassistant'] != null
        ? new TeachingAssistant.fromJson(json['teachingassistant'])
        : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.instructor != null) {
      data['instructor'] = this.instructor.toJson();
    }
    if (this.teachingassistant != null) {
      data['teachingassistant'] = this.teachingassistant.toJson();
    }
    return data;
  }
}

class Instructor {
  String instructorId;

  Instructor({this.instructorId});

  Instructor.fromJson(Map<String, dynamic> json) {
    instructorId = json['instructor_id'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['instructor_id'] = this.instructorId;
    return data;
  }
}

class TeachingAssistant {
  String teachingAssistantId;

  TeachingAssistant({this.teachingAssistantId});

  TeachingAssistant.fromJson(Map<String, dynamic> json) {
    teachingAssistantId = json['teaching_assistant_id'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['teaching_assistant_id'] = this.teachingAssistantId;
    return data;
  }
}
