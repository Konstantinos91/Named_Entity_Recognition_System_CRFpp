
#The following command has to be typed in the linux terminal in order to run this preprocessing script of the corpus and save the output: perl preprocessing_traincorpus.pl traincorpus > preprocessed_traincorpus  

#in the event that there are errors in the executable code, and will end the execution. 
use strict;

#It only warns when there is a mistake in the code but does not stop the execution
use warnings;

my @wcorpus;

#Checks if the corpus file is empty or not in order to proceed to the preprocessing phase.
if (scalar @ARGV < 1) {
die "Input error! Check the corpus file!";
}

#It opens and reads the corpus
open (my $Inputf, '<', $ARGV[0]) or die $!;



my $largest_corpus_columns = 0;
while (<$Inputf>) {  #While the corpus file has not been scanned and therefore, the "(<$Inputf>)" is true, it proceeds to the loop execution in order to create an additional column in the corpus and print it.
  chomp;  #to get rid of the newline (\n) from the end of the input corpus.
  @wcorpus = split /\s+/; #Regex for split with whitespace.
  foreach my $wcomponent (@wcorpus) { 
    my $corpus_columns = $wcomponent =~ s/\|/\t/g; #Regex for replacement with tab space.
    $largest_corpus_columns = $corpus_columns > $largest_corpus_columns ? $corpus_columns : $largest_corpus_columns;
    print "$wcomponent\n";
  }
  print "\n";
}
close ($Inputf); 

