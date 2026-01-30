const ko = require("knockout");

var ProjectView = function(config) {
  var self = this;
  var config = config || {};

  self.projects = ko.observableArray(
    ko.utils.arrayMap(config.projects, function(project) {
      return new ProjectModel(project);
    })
  );
};

var ProjectModel = function(data) {
  var self = this;
  var data = data || {};

  self.name = ko.observable(data.name);
  self.meta = ko.observable(data.meta);
  self.description = ko.observable(data.description);
  self.url = ko.observable(data.url);
  self.versions = ko.observableArray(
    ko.utils.arrayMap(data.versions, function (version) {
      return new VersionModel({
        project: self,
        version: version.version,
        language: version.language,
      });
    })
  );
  self.topics = ko.observableArray(data.topics || []);
  self.show_topics = ko.computed(function () {
    var topics = self.topics();
    return (typeof topics !== 'undefined' && topics.length > 0);
  });
};

var VersionModel = function(data) {
  var self = this;
  var data = data || {};

  self.project = data.project;
  self.version = ko.observable(data.version || "latest");
  self.language = ko.observable(data.language || "en");
  self.show_language = ko.computed(function () {
    return self.language() !== "en";
  });
  self.url = ko.computed(function () {
    var url = self.project.url();
    if (!url.endsWith("/")) {
      url += "/";
    }
    url += self.language() + "/" + self.version() + "/";
    return url;
  });
};

ProjectView.init = function(projects) {
  $(document).ready(function() {
    var view = new ProjectView({
      projects: projects,
    });
    ko.applyBindings(view, $("#docs-projects").get(0));
    return view;
  });
};

// Export this globally so that we can load the project data from a separate
// file. Eventually this should be loaded from an API endpoint instead.
global.ProjectView = ProjectView;
