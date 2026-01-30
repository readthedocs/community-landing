// Minimal $ helper for this landing page (no jQuery dependency).
(function () {
  if (window.$) {
    return;
  }

  function ready(callback) {
    if (document.readyState !== "loading") {
      callback();
    } else {
      document.addEventListener("DOMContentLoaded", callback);
    }
  }

  function $(selector) {
    if (selector === document) {
      return { ready: ready };
    }

    var nodes =
      typeof selector === "string"
        ? document.querySelectorAll(selector)
        : [selector];

    return {
      get: function (index) {
        return nodes[index];
      },
    };
  }

  window.$ = $;
})();
