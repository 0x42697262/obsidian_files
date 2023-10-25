

[F, C] = all_hand_features;

%cplot(F(:,1:3),C);
[Cest, Ctrue] = all_hand_classify(F, C, 3);