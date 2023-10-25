%
% TEST SCRIPT FOR MPEG ENCODING ASSIGMENT 
%

load newsreader

BLANK=zeros(size(IMGS,1),size(IMGS,2));
encode_reference= BLANK;
decoded_imagery  = BLANK; 

tolerance=input('Enter change tolerance (def. 5): ');
if (isempty(tolerance));tolerance=5;end
Q=input('Enter encoding quality (def. 80): ');
if (isempty(Q));Q=80;end;
yn=input('Pause after each frame? (def. y): ','s');
if (isempty(yn));dopause=true;else;dopause=(yn(1)=='y');end

encoded_total_bytes = 0;
input_total_bytes = 0;

figure(1); 
colormap(gray);

% comment out
clear MOV;

for i=1:size(IMGS,3) 
  input_image = IMGS(:,:,i);
  % encoding STAGE
  input_total_bytes = input_total_bytes + numel(input_image);
  if ( rem(i-1,10)==0 )
    % keyframe (compress entire image. The -999 tolerance forces this)
    [H,encode_reference] = simple_mpeg(input_image,encode_reference,Q,-999);
    fprintf(1,'%02d Keyframe (%d bytes)\n',i,length(H));
  else
	% difference frame (compress only differences)
    [H,encode_reference] = simple_mpeg(input_image,encode_reference,Q,tolerance);
    fprintf(1,'%02d Differences (%d bytes)\n',i,length(H));
  end
  % decoding STAGE
  encoded_total_bytes = encoded_total_bytes + length(H);
  
  % generate decoding of only the regions transmitted (for display only. this
  % is not normally generated in practice)
  change_imagery = simple_dmpeg(H,BLANK,Q); 
  
  % generate decoding of the reconstructed images
  decoded_imagery = simple_dmpeg(H,decoded_imagery,Q); 
  
  figure(1);
  subplot(2,2,1);
  imagesc(input_image); title(sprintf('Input %2d (%d bytes total)',i,input_total_bytes));
  subplot(2,2,2);
  imagesc(encode_reference); title('Ref');
  subplot(2,2,3);
  imagesc(change_imagery); title( sprintf('Transmitted Data (%d bytes)',length(H)));
  xlabel( sprintf('Q = %d, Tolerance = %3.2f',Q,tolerance) );
  subplot(2,2,4);
  imagesc(decoded_imagery); 
  title(sprintf('Reconstructed (%d bytes total)',encoded_total_bytes)); 
  drawnow; 

  % comment out
  MOV(i) = getframe(1);
  
  if (dopause)
    disp('Press a key to continue');
    pause
  end
end
