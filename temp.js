
router.route('/reset-password/:email/:token').patch(resetPasswordController);


const resetPasswordController = async (req, res) => {
    const { email, token } = req.params;
    const { password } = req.body;
  
    if (!email || !token) throw new BadRequest('required data not sent with url');
  
    const user = await User.findOne({
      passwordResetToken: token,
      passwordResetExpires: { $gt: Date.now() },
    });
  
    if (!user) throw new BadRequest('No user found with this token');
  
    if (!password) throw new BadRequest('Password field is needed');
  
    const hashedPassword = await bcrypt.hash(password, 10);
  
    user.password = hashedPassword;
    user.passwordResetExpires = undefined;
    user.passwordResetToken = undefined;
  
    const result = await user.save();
  
    return res.status(StatusCodes.OK).json({ message: 'The password has been changed.' });
};

module.exports = {
    
  resetPasswordController,
}