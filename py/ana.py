import ROOT 
from ROOT import TFile, TH1F, TF1

h = TH1F("myHist", "myTitle", 64, -4, 4)

output = TFile("Dielectron_MC.root", "Recreate"); 

el1_eta = TH1F("el1_eta", "Pseudorapidity of the most energetic electron candidate", 100, -5, 5);
el2_eta = TH1F("el2_eta", "Pseudorapidity of the second most energetic electron candidate", 100, -4, 4);
el1_pt =  TH1F("el1_pt", "pT of the most energetic electron candidate", 100, 0, 200);
el2_pt = TH1F("el2_pt", "pT of the second most energetic electron candidate", 100, 0, 200);
Z_ee =  TH1F("Z_ee", "Di-electron candidate invariant mass", 200, 0, 200);

sqroot = TF1( 'sqroot', 'x*gaus(0) + [3]*form1', 0, 10 )

el1_eta.FillRandom("sqroot",1000)
el1_eta.SetFillColor( 45 )
el1_eta.Draw()
