Feature: search for multiple pages and open them 

  Scenario: try to search for GitHub and open the first result
     Given open prowser
     When open google "yputube"
     And open the page
     Then wait and close
     Then last
     Then last2
     Then quit

  Scenario: try to search for YouTube and open the first result
     Given open prowser
     When open google "GitHub"
     And open the page
     Then wait and close
     Then quit
