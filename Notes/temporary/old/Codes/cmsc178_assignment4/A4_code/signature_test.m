% TEST SCRIPT FOR SIGNATURE CREATION

disp('This test script will create a signature for 3 images in the dataset');

I=double( imread(['rock' filesep 'rock_0041.png'])) / 255;
B=hand_extract(I);
S_rok = hand_signature(B);

figure; colormap(gray);
subplot(2,2,1);
imagesc(B); title('Binary Region - rock');
subplot(2,1,2);
plot(S_rok); title('Signature');
xlabel('Angle (deg)');
ylabel('Distance');
drawnow;

I=double( imread(['paper' filesep 'paper_0041.png'])) / 255;
B=hand_extract(I);
S_pap = hand_signature(B);

figure; colormap(gray);
subplot(2,2,1);
imagesc(B); title('Binary Region - paper');
subplot(2,1,2);
plot(S_pap); title('Signature');
xlabel('Angle (deg)');
ylabel('Distance');
drawnow;

I=double( imread(['scissors' filesep 'scissors_0041.png'])) / 255;
B=hand_extract(I);
S_sci = hand_signature(B);

figure; colormap(gray);
subplot(2,2,1);
imagesc(B); title('Binary Region - scissors');
subplot(2,1,2);
plot(S_sci); title('Signature');
xlabel('Angle (deg)');
ylabel('Distance');
drawnow;