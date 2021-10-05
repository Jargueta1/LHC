import os, sys
import ROOT


# To run, do "python <path-to>/demo.py"
 
# enable running from another directory than the one where demo.py resides
workdir = os.path.dirname( sys.argv[0] )
if workdir:
   os.chdir( workdir )
 
# This macro generates a Controlbar menu.
# To execute an item, click with the left mouse button.
# To see the HELP of a button, click on the right mouse button.
 
ROOT.gStyle.SetScreenFactor(1)   # if you have a large screen, select 1.2 or 1.4
 
bar = ROOT.TControlBar( 'vertical', 'Demos', 10, 10 )
 
# The callbacks to python work by having CLING call the python interpreter through
# the "TPython" class. Note the use of "raw strings."
if sys.version_info[0] > 2:
    to_run = 'exec(open(\'{}\').read())'
else:
    to_run = 'execfile(\'{}\')'
 
bar.AddButton( 'Help on Demos', r'TPython::Exec( "' + to_run.format('demoshelp.py') + '" );', 'Click Here For Help on Running the Demos' )
bar.AddButton( 'Help on Demos', r'TPython::Exec( "' + to_run.format('ana.py') + '" );', 'Click Here For Help on Running the Demos' )
bar.AddButton( 'browser',       r'TPython::Exec( "b = ROOT.TBrowser()" );',          'Start the ROOT browser' )
 
bar.Show()
 
ROOT.gROOT.SaveContext()
 
 
## wait for input to keep the GUI (which lives on a ROOT event dispatcher) alive
if __name__ == '__main__':
   rep = ''
   while not rep in [ 'q', 'Q' ]:
      # Check if we are in Python 2 or 3
      if sys.version_info[0] > 2:
         rep = input( 'enter "q" to quit: ' )
      else:
         rep = raw_input( 'enter "q" to quit: ' )
      if 1 < len(rep):
         rep = rep[0]