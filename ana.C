#define ana_cxx
#include "ana.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void ana::Loop()
{
//   In a ROOT session, you can do:
//      root> .L ana.C
//      root> ana t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;
   
   // Declare histograms
    TH1F* el1_eta = new TH1F("el1_eta", "Pseudorapidity of the most energetic electron candidate"
    , 100, -4, 4);
    TH1F* el2_eta = new TH1F("el2_eta", "Pseudorapidity of the second most energetic electron candidate"
    , 100, -4, 4);
    
    TH1F* el1_pt = new TH1F("el1_pt", "pT of the most energetic electron candidate", 100, 0, 200);
    TH1F* el2_pt = new TH1F("el2_pt", "pT of the second most energetic electron candidate", 100, 0, 200);

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      el1_eta->Fill(f_lept1_eta);
      el2_eta->Fill(f_lept2_eta);
      el1_pt->Fill(f_lept1_pt);
      el2_pt->Fill(f_lept2_pt);

   }
}
