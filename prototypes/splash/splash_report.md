# Splash Report

## Bugs
- [ ] When creating company files there is no normalization of input by the user
    - It should protect against the following:
       - [ ] Large filenames (give a max size)
       - [ ] Use of escape characters
       - [ ] Wheter or not file already exits in directory
- [ ] Adding a new company does not update the dropdown menu until app is restarted
- [ ] About text is just a placeholder
- [ ] Open button allows you to choose open a blank file
- [ ] You can open multiple top level windows
- [ ] Records & paycheck windows just have placeholder information

## Insights

<p> Moving forward I might need to seperate out all of the command functions into a seperate module, and import them in for readability reasons. Eventually I think it would also be largely benefical to put objects into their own classes. Possibly seperated by windows (splash, record display, paycheck calculator). I'm also still not to sure about opening the paycalc in a new window using the topLevel class (at least not the way it is written now). Maybe refactoring that is in the futute.</p>

## Next Steps

- [ ] Create the payroll data, so that it can be used for record functionalities
- [ ] Refactor paycalc so that it can interact with other aspects of the app easier (Class?)
- [ ] Fix all those bugs! :bug:
