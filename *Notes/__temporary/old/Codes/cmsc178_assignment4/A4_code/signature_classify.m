%
% SIGNATURE CLASSIFICATION CODE - DO NOT EDIT
%

% STEP 1 - get signatures of 3 examples from the training data

I=double( imread([ 'rock' filesep 'rock_0041.png']) ) / 255;
B=hand_extract(I);
S_rok = hand_signature(B);
disp('Rock Reference Signature created...');
pause(1)

I=double( imread([ 'paper' filesep 'paper_0041.png']) ) / 255;
B=hand_extract(I);
S_pap = hand_signature(B);
disp('Paper Reference Signature created...');
pause(1)

I=double( imread(['scissors' filesep 'scissors_0041.png']) ) / 255;
B=hand_extract(I);
S_sci = hand_signature(B);
disp('Scissors Reference Signature created...');
pause(1);

disp('Starting classifier in 3 seconds...');
pause(3);
%
% STEP 2 - for each image compare to the 3 reference signatures
%
dn={ 'rock' 'paper' 'scissors'};
C=[];
Cest=[];
Ctru=[];
% foreach durectory
for rps=1:3
  dd=dn{rps};
  d=dir( [ dd filesep '*.png' ]);
  % for each file in directory
  for i=1:length(d)
    I = double( imread( [ dd filesep d(i).name ] ) ) / 255;
    B = hand_extract(I);
    S = hand_signature(B);
    
    % MIN DISTANCE METHOD
    XCr=[];XCp=[];XCs=[];
    
    % regularise w.r.t mean distance
    S_m    = S/mean(S);
    S_rok_m = S_rok/mean(S_rok);
    S_pap_m = S_pap/mean(S_pap);
    S_sci_m = S_sci/mean(S_sci);
      
    % for each circ shift find sum abs difference
    for k=0:(length(S_m)-1)
      Ss=circshift(S_m,[0 k]);
      XCr(k+1)= sum( abs(Ss-S_rok_m) );
      XCp(k+1)= sum( abs(Ss-S_pap_m) );
      XCs(k+1)= sum( abs(Ss-S_sci_m) );
    end
    % find min distances to each signature
    Cr=min(XCr);
    Cp=min(XCp);
    Cs=min(XCs);
 
    % identify minimum distance (ie closest matching reference)
    [mx,ind]=min([Cr Cp Cs]);
    
    % update result arrays
    C(end+1,:)=[Cr Cp Cs];
    Cest(end+1) = ind;
    Ctru(end+1) = rps;
    
    % DISPLAY A MATCH PLOT FOR EACH SAMPLE
    figure(111);
    subplot(2,4,1); plot(S); title('Test Sig');  a=axis; axis([a(1:2) 0 a(4)]);
    subplot(2,4,2); plot(S_rok); title('Rock'); a=axis; axis([a(1:2) 0 a(4)]);
    subplot(2,4,3); plot(S_pap); title('Paper'); a=axis; axis([a(1:2) 0 a(4)]);
    subplot(2,4,4); plot(S_sci); title('Scissors'); a=axis; axis([a(1:2) 0 a(4)]);
    subplot(2,4,5:8);
    plot(XCr,'r'); hold on
    plot(XCp,'g'); hold on
    plot(XCs,'b'); hold off
    title( sprintf('Scores: best match is "%s"',dn{ind}) );
    xlabel('Circular Shift Offset');
    ylabel('Sum Abs Distance');
    drawnow;
    
  end
end

% DISPLAY FINAL MATCH RESULTS

figure
plot(Ctru);
hold on
plot(Cest,'ro');
hold off
title( sprintf('True versus Matched (%3.1f%% correct)',100*sum(Ctru==Cest)/length(Ctru)) );
legend('C true','C matched');
xlabel('Sample No');
ylabel('Class');
drawnow;

  
